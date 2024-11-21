# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from sphinx.builders.html import StandaloneHTMLBuilder
import subprocess, os, sys
sys.path.insert(0, os.path.abspath('.'))

# Doxygen
subprocess.call('doxygen Doxyfile', shell=True)

# -- Project information -----------------------------------------------------
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CGNS'
# copyright is overridden by '_static/css/copyright.css'
# see https://github.com/readthedocs/sphinx_rtd_theme/issues/828
copyright = ""
#author = 'CGNS'

# -- General configuration ---------------------------------------------------
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_sitemap',
    'sphinx.ext.inheritance_diagram',
    'sphinxfortran.fortran_domain',
    'sphinxfortran.fortran_autodoc',
    'breathe'
]
# Prefix to add to ticket numbers to get the full URL to JIRA
# see use in the News page
extlinks = {
    'issue': ('https://cgnsorg.atlassian.net/projects/CGNS/issues/%s', '#%s'),
    'version': ('https://github.com/CGNS/CGNS/releases/tag/%s', 'version%s')}

#suppress_warnings = [ 'image.not_readable' ]
suppress_warnings = ['autosectionlabel.*']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

highlight_language = 'c'
pygments_style = 'sphinx'

# adding Lexer
from sphinx.highlighting import lexers
import sys
sys.path.append('.')
from sidslexer import SidsLexer

lexers["sids"] = SidsLexer()

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_css_files = [
    'css/custom.css',
]

#html_theme = 'alabaster'
html_static_path = ['_static']

##html_permalinks_icon = '<span>#</span>'
#html_theme = 'sphinxawesome_theme'

#MSB import guzzle_sphinx_theme
#MSBhtml_theme_path = guzzle_sphinx_theme.html_theme_path()
#MSBhtml_theme = 'guzzle_sphinx_theme'

html_theme = 'conestack'
#
html_theme_options = {
    'cs_color': '#260078',
    'cs_bg_color': 'var(--bs-indigo)',
    'logo_url': '_static/cgns_color_home.svg',
    'logo_title': ' ',
    'logo_width': '78px',
    'logo_height': '66px',
    'github_url': 'https://github.com/CGNS/CGNS'
}

#html_theme_options = {
#    'cs_color': '#F0F8FF',
#    'cs_bg_color': '#F0F8FF'
#    'logo_url': '_static/your_logo.svg',
#    'logo_title': 'CGNS/MLL - An API for C and Fortran applications',
#    'logo_width': '40px',
#    'logo_height': '40px'
#}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
#html_theme_options = {
#    'canonical_url': '',
#    'analytics_id': '',
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'logo_only': False,
    # Toc options
#    'collapse_navigation': True,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False
#}
# html_logo = ''
# github_url = ''
# html_baseurl = 'https://docs.example.org/doc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/copyright.css",
]
fortran_src = ["../src/c.F90"]
fortran_subsection_type = "title"
# -- Breathe configuration -------------------------------------------------

breathe_projects = {
        "CGNS Sphinx Doxygen Breathe": "./xml"
}
#breathe_implementation_filename_extensions = ['.c']
breathe_domain_by_extension = {"h" : "c"}
breathe_default_project = "CGNS Sphinx Doxygen Breathe"
breathe_default_members = ('members', 'undoc-members')

