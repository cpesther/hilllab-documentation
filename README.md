# HillLab documentation website

A minimal Markdown documentation site built with Jekyll and GitHub's Minimal theme.
The site currently contains only a placeholder home page; no module documentation has been added.

## Publish on GitHub Pages

1. Commit and push these files to the `main` branch of `cpesther/hilllab-documentation`.
2. In the repository, open **Settings → Pages** and select **GitHub Actions** as the source.
3. Run **Deploy documentation to GitHub Pages** from the **Actions** tab, or push another change to `main`.

Once deployment succeeds, the site will be available at:
<https://cpesther.github.io/hilllab-documentation/>.

See [GitHub's Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Edit the site

- `index.md` is the Markdown home page.
- `_config.yml` contains the site title, theme, and URL settings.
- `.github/workflows/pages.yml` builds and deploys the site.

Future pages can be written as `.md` files with Jekyll front matter, using `layout: default` and a page `title`.
Use Jekyll's `relative_url` filter for internal links so they work under `/hilllab-documentation/`.

## Optional local preview

With a supported Ruby version and Bundler installed, run:

```sh
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000/hilllab-documentation/>.
The GitHub Actions build uses preinstalled GitHub Pages dependencies and does not require a local Ruby installation.
