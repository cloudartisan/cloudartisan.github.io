"""Exercise the checker CLI against disposable rendered-site fixtures."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).with_name("check_internal_links.py")


class InternalLinksTest(unittest.TestCase):
    def run_checker(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(CHECKER), str(root), "--base-url", "https://cloudartisan.com/"],
                capture_output=True, text=True,
            )

    def test_missing_article_routes_fail_with_source_and_target(self):
        result = self.run_checker({"index.html": '<a href="http://www.cloudartisan.com/2010/10/old/">Old</a>'})
        self.assertEqual(result.returncode, 1)
        self.assertIn("index.html:1", result.stdout)
        self.assertIn("/2010/10/old/", result.stdout)

    def test_current_relative_encoded_and_absolute_links_pass(self):
        result = self.run_checker({
            "index.html": '<a href="/posts/article/?utm=x#section">Post</a><a href="//www.cloudartisan.com/feed.xml">Feed</a>',
            "posts/article/index.html": '<a href="../../about/">About</a><img src="/images/my%20image.png"><script src="/app.js"></script>',
            "about/index.html": '<a href="mailto:hello@example.com">Email</a><a href="https://example.com/missing">External</a><a href="#top">Top</a>',
            "feed.xml": "<rss/>", "images/my image.png": "image", "app.js": "",
        })
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_assets_and_srcset_candidates_fail(self):
        for markup, missing in [
            ('<img src="/missing.png">', "/missing.png"),
            ('<source srcset="/exists.png 1x, /missing.png 2x">', "/missing.png"),
            ('<link rel="stylesheet" href="/missing.css">', "/missing.css"),
            ('<script src="/missing.js"></script>', "/missing.js"),
        ]:
            with self.subTest(markup=markup):
                result = self.run_checker({"index.html": markup, "exists.png": "image"})
                self.assertEqual(result.returncode, 1)
                self.assertIn(missing, result.stdout)

    def test_redirect_target_must_exist(self):
        result = self.run_checker({"index.html": '<meta http-equiv="refresh" content="0; url=https://cloudartisan.com/missing/">'})
        self.assertEqual(result.returncode, 1)
        self.assertIn("/missing/", result.stdout)

    def test_trailing_slash_cannot_turn_an_existing_file_into_a_route(self):
        for target in ("/feed.xml/", "/feed.xml/?source=test", "/image.png/", "/feed.xml%2F"):
            with self.subTest(target=target):
                result = self.run_checker({
                    "index.html": f'<a href="{target}">File</a>',
                    "feed.xml": "<rss/>", "image.png": "image",
                })
                self.assertEqual(result.returncode, 1)
                self.assertIn(target, result.stdout)

    def test_alias_redirect_and_data_images_pass(self):
        result = self.run_checker({
            "index.html": '<meta http-equiv="refresh" content="0; url=https://cloudartisan.com/new/"><link rel="canonical" href="/new/">',
            "new/index.html": '<img srcset="data:image/png;base64,AAAA 1x, /image.png 2x">',
            "image.png": "image",
        })
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_localhost_links_fail_even_when_path_exists(self):
        result = self.run_checker({"index.html": '<a href="http://localhost:1313/">Local</a>'})
        self.assertEqual(result.returncode, 1)
        self.assertIn("localhost", result.stdout)

    def test_non_default_site_ports_fail_even_when_route_exists(self):
        for target in ("https://cloudartisan.com:1313/about/", "http://www.cloudartisan.com:443/about/", "https://cloudartisan.com:0/about/"):
            with self.subTest(target=target):
                result = self.run_checker({
                    "index.html": f'<a href="{target}">About</a>',
                    "about/index.html": "<html></html>",
                })
                self.assertEqual(result.returncode, 1)
                self.assertIn(target, result.stdout)

    def test_explicit_default_site_ports_pass(self):
        result = self.run_checker({
            "index.html": '<a href="https://cloudartisan.com:443/about/">HTTPS</a><a href="http://www.cloudartisan.com:80/about/">HTTP</a>',
            "about/index.html": "<html></html>",
        })
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_base_element_changes_relative_link_resolution(self):
        result = self.run_checker({"index.html": '<base href="/posts/"><a href="missing/">Missing</a>'})
        self.assertEqual(result.returncode, 1)
        self.assertIn("/posts/missing/", result.stdout)

    def test_sitemap_missing_page_fails(self):
        result = self.run_checker({
            "index.html": "<html></html>",
            "sitemap.xml": '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://cloudartisan.com/missing/</loc></url></urlset>',
        })
        self.assertEqual(result.returncode, 1)
        self.assertIn("sitemap.xml", result.stdout)
        self.assertIn("/missing/", result.stdout)

    def test_empty_build_fails(self):
        result = self.run_checker({})
        self.assertEqual(result.returncode, 1)
        self.assertIn("HTML", result.stdout)


if __name__ == "__main__":
    unittest.main()
