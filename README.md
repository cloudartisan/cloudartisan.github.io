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

## Building for Production

```
hugo
```

This will generate the static site in the `public` directory.

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## License

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

My blog content, posts, etc are licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
