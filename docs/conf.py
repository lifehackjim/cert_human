"""Sphinx conf.py."""
from __future__ import absolute_import, division, print_function, unicode_literals

import sys

import sphinx_bootstrap_theme

try:
    import pathlib
except Exception:
    import pathlib2 as pathlib

THIS_FILE = pathlib.Path(__file__).absolute()
THIS_PATH = THIS_FILE.parent
TOOL_PATH = THIS_PATH.parent

if TOOL_PATH not in sys.path:
    sys.path.insert(0, format(TOOL_PATH))

import cert_human as pkg  # noqa

# sphinx config ref: http://www.sphinx-doc.org/en/master/usage/configuration.html

project = pkg.__name__
author = pkg.__author__
version = pkg.__version__
release = pkg.__version__
copyright = pkg.__copyright__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]  # Sphinx extension modules: http://www.sphinx-doc.org/en/master/usage/extensions/index.html

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

master_doc = "index"  # The master toctree document.
language = "en"  # The language for content autogenerated by Sphinx
todo_include_todos = True  # If true, `todo` and `todoList` produce output
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_templates", "_themes"]
html_static_path = ["_static"]
html_show_sourcelink = False  # do not show a link to the RST source for each page
html_show_sphinx = False  # do not show built by sphinx line
html_last_updated_fmt = "%b %d, %Y"
autodoc_default_options = {
    'member-order': 'bysource',
}

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    # 'navbar_title': "Demo",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "TOC",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        # ("Examples", "examples"),
        # ("Link", "http://example.com", True),
        ("Repository", "https://github.com/lifehackjim/cert_human", True),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': -1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "cosmo" or "sandstone".
    #
    # The set of valid themes depend on the version of Bootstrap
    # that's used (the next config option).
    #
    # Currently, the supported themes are:
    # - Bootstrap 2: https://bootswatch.com/2
    # - Bootstrap 3: https://bootswatch.com/3
    'bootswatch_theme': "united",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
    "requests": ("http://docs.python-requests.org/en/master/", None),
    "asn1crypto": ("https://www.pydoc.io/pypi/asn1crypto-0.24.0", None),
    "pyopenssl": ("https://pyopenssl.org/en/stable/", None),
    "urllib3": ("https://urllib3.readthedocs.io/en/latest/", None),
}
