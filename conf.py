"""Sphinx configuration for the Markdown documentation site."""

project = "HillLab"
language = "en"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
]

# Author pages in Markdown; autosummary uses reStructuredText for generated stubs.
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
root_doc = "index"
toc_object_entries = False
add_module_names = False
exclude_patterns = ["_build", "_authoring", ".venv", "README.md", ".DS_Store"]
myst_enable_extensions = ["colon_fence", "fieldlist", "dollarmath", "amsmath"]

# Ready for API pages when the Python package is installed in the build environment.
autodoc_typehints = "description"
autodoc_member_order = "bysource"
napoleon_numpy_docstring = True
napoleon_google_docstring = True

html_theme = "pydata_sphinx_theme"
html_title = "HillLab documentation"
html_baseurl = "https://cpesther.github.io/hilllab-documentation/"
html_context = {"default_mode": "dark"}
html_theme_options = {
    "logo": {"text": "HillLab"},
    "github_url": "https://github.com/cpesther/hilllab-documentation",
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "show_prev_next": False,
}
html_theme_options.update({"navigation_depth": 4, "show_toc_level": 2})
html_show_sourcelink = False
html_show_copyright = False
html_static_path = ["_static"]
html_css_files = ["reference.css"]
pygments_style = "friendly"
pygments_dark_style = "monokai"
