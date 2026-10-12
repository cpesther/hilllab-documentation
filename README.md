# HillLab documentation website

A Markdown documentation site built with Sphinx, MyST, and the
[PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).
The theme defaults to dark mode and includes a light/dark toggle, search,
navigation, and syntax highlighting. It is the theme used by Seaborn and the
basis for Matplotlib's documentation theme.

The site currently contains only a placeholder home page; no module documentation has been added.

## Publish on GitHub Pages

1. Commit and push these files to the `main` branch of `cpesther/hilllab-documentation`.
2. In the repository, open **Settings → Pages** and select **GitHub Actions** as the source.
3. Run **Deploy documentation to GitHub Pages** from the **Actions** tab, or push another change to `main`.

Once deployment succeeds, the site will be available at:
<https://cpesther.github.io/hilllab-documentation/>.

The workflow installs the pinned Python dependencies, builds the site with
warnings treated as errors, and deploys the generated HTML. Sphinx also creates
the `.nojekyll` file needed to serve its underscore-prefixed asset directories.

## Edit the site

- `index.md` is the Markdown home page.
- `conf.py` contains the theme and Sphinx configuration.
- `requirements.txt` contains the documentation build dependencies.
- `.github/workflows/pages.yml` builds and deploys the site.

Write future pages in [MyST Markdown](https://myst-parser.readthedocs.io/en/stable/)
and link them from a `toctree` directive in `index.md` when they are ready.
Ordinary Markdown headings, links, and fenced Python code blocks work directly.
MyST also supports Sphinx directives and cross-references for documenting
functions, classes, parameters, return values, and variables.

The configuration enables `autodoc`, `autosummary`, and `napoleon` for future API
documentation, including NumPy and Google style docstrings. Before adding
`autofunction`, `autoclass`, or `autodata` directives, install HillLab and its
dependencies in the documentation build environment, both locally and in CI.
Wrap autodoc directives in a MyST `eval-rst` fence so their generated
reStructuredText is parsed correctly within a Markdown page.
The placeholder site does not import or require the module.

## Local preview

With Python 3.14 installed, run:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m sphinx -b html -W --keep-going . _build/html
python -m http.server 8000 --directory _build/html
```

Open <http://localhost:8000/>. Rebuild with the Sphinx command after editing pages.
