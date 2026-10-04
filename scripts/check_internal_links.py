"""Check same-site HTML links and sitemap entries against rendered Hugo output.

Offline and dependency-free. Does not check external sites, fragment identifiers,
CSS url() values, or URLs constructed by JavaScript.
"""

import argparse
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


def srcset_urls(value):
    """Read URL tokens without splitting commas embedded in data URLs."""
    while value:
        value = value.lstrip(" \t\r\n\f,")
        if not value:
            return
        parts = value.split(None, 1)
        url = parts[0]
        value = parts[1] if len(parts) > 1 else ""
        yield url.rstrip(",")
        if not url.endswith(","):
            # Skip descriptors up to the next candidate separator.
            value = value.partition(",")[2]


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.base = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "base":
            if self.base is None:
                self.base = attrs.get("href")
            return
        for name in ("href", "src", "poster", "action"):
            if attrs.get(name):
                self.links.append((self.getpos()[0], attrs[name]))
        if attrs.get("srcset"):
            self.links.extend((self.getpos()[0], url) for url in srcset_urls(attrs["srcset"]))
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            match = re.search(r";\s*url\s*=\s*(.+)", attrs.get("content", ""), re.I)
            if match:
                self.links.append((self.getpos()[0], match[1].strip().strip("\"'")))


def check_site(root, base_url):
    root = root.resolve()
    host = urlsplit(base_url).hostname
    if not host or urlsplit(base_url).scheme not in ("http", "https"):
        raise ValueError("--base-url must be an absolute HTTP(S) site URL")
    host = host.removeprefix("www.")
    internal_hosts = {host, "www." + host}
    errors = []
    checked = 0

    def check_link(source, line, raw, document_url):
        nonlocal checked
        url = urlsplit(urljoin(document_url, raw))
        if url.hostname in {"localhost", "127.0.0.1", "::1"}:
            errors.append(f"{source}:{line}: local development URL {raw}")
            return
        if url.scheme not in ("http", "https") or url.hostname not in internal_hosts:
            return
        checked += 1
        default_port = 443 if url.scheme == "https" else 80
        if url.port not in (None, default_port):
            errors.append(f"{source}:{line}: non-default site port in {raw}")
            return
        decoded_path = unquote(url.path)
        destination = (root / decoded_path.lstrip("/")).resolve()
        # A trailing slash requests a directory route, even if Path normalises
        # it to an existing file (e.g. /feed.xml/ is not /feed.xml).
        file_exists = not decoded_path.endswith("/") and destination.is_file()
        if not destination.is_relative_to(root) or not (
            file_exists or (destination / "index.html").is_file()
        ):
            errors.append(f"{source}:{line}: missing destination {raw} (resolved to {url.path})")

    html_files = sorted(root.rglob("*.html"))
    if not (root / "index.html").is_file() or not html_files:
        return ["Build output must contain an HTML homepage (index.html)"], 0
    for path in html_files:
        source = path.relative_to(root).as_posix()
        document_path = source.removesuffix("index.html") if path.name == "index.html" else source
        document_url = urljoin(base_url, document_path)
        parser = LinkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        effective_base = urljoin(document_url, parser.base) if parser.base else document_url
        for line, raw in parser.links:
            check_link(source, line, raw, effective_base)
    for path in sorted(root.rglob("*sitemap*.xml")):
        source = path.relative_to(root).as_posix()
        try:
            tree = ET.parse(path)
        except ET.ParseError as error:
            errors.append(f"{source}: invalid sitemap XML: {error}")
            continue
        for entry in tree.iter():
            if entry.tag.rsplit("}", 1)[-1] == "loc" and entry.text:
                check_link(source, 1, entry.text.strip(), base_url)
    return errors, checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, nargs="?", default=Path("public"))
    parser.add_argument("--base-url", required=True, help="Hugo production baseURL")
    args = parser.parse_args()
    try:
        errors, checked = check_site(args.directory, args.base_url)
    except (ValueError, OSError) as error:
        print(f"Cannot check build output: {error}")
        return 1
    for error in errors:
        print(error)
    print(f"Checked {checked} internal references; {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
