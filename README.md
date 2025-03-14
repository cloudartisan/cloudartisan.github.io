# Cloud Artisan Blog

Personal blog and project showcase for David Taylor (Cloud Artisan).

## Technology

This site is built with:
- [Hugo](https://gohugo.io/) - A fast and modern static site generator
- [Congo Theme](https://github.com/jpanther/congo) - A powerful, lightweight theme for Hugo

## Local Development

1. Clone this repository:
   ```
   git clone https://github.com/cloudartisan/cloudartisan.github.io.git
   cd cloudartisan.github.io
   ```

2. Install Hugo:
   ```
   brew install hugo
   ```

3. Run the local development server:
   ```
   hugo server -D
   ```

4. View the site at http://localhost:1313/

## Creating Content

### New Posts
```
hugo new content posts/my-new-post.md
```

### New Projects
```
hugo new content projects/project-name.md
```

## Maintenance Scripts

The repository includes several maintenance scripts in the `scripts/` directory:

- `fix_backticks.py` - Fixes inline code formatting issues in markdown files
- `fix_twitter_links.py` - Updates Twitter links from HTTP to HTTPS
- `fix_links.py` - Template for fixing various broken links

To run a script:
```
python3 -m venv venv          # Create virtual environment (first time only)
source venv/bin/activate      # Activate virtual environment
pip install pyyaml            # Install dependencies (first time only)
python3 scripts/script_name.py   # Run the script
```

## Building for Production

```
hugo
```

This will generate the static site in the `public` directory.

## Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions when changes are pushed to the main branch. The workflow:

1. Builds the Hugo site using Hugo modules
2. Deploys the generated files to the gh-pages branch
3. GitHub Pages then serves the content from the gh-pages branch

To configure GitHub Pages:
1. Go to repository Settings > Pages
2. Set the source to "Deploy from a branch"
3. Select the "gh-pages" branch and "/" (root) folder
4. Save the settings

Note: The site uses two workflows - "Deploy Hugo site" builds the site, and "pages-build-deployment" handles the GitHub Pages publishing.

## License

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

My blog content, posts, etc are licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
