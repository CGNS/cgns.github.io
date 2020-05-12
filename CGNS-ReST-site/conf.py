# CGNS Documentation files
# See LICENSING/COPYRIGHT at root dir of this documentation sources
#
# --- Project information -----------------------------------------------------
project = 'CGNS'
copyright = '1991-2020, CGNS Steering Commmittee'
author = 'CGNS Steering Committee'
version = '4.0'   # The short X.Y version
release = '4.0.0' # The full version, including alpha/beta/rc tags

# --- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
]
# Prefix to add to ticket numbers to get the full URL to JIRA
# see use in the News page
extlinks = {
    'issue': ('https://cgnsorg.atlassian.net/projects/CGNS/issues/', '#'),
    'version': ('https://github.com/CGNS/CGNS/releases/tag/', 'version ')}

# --- sphinx code generation params
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['build']
pygments_style = 'sphinx'

import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
# CGNS is based on the guzzle theme
extensions.append("guzzle_sphinx_theme")

# --- Options for HTML output 
html_favicon =  'images/logo/CGNS_tiny.ico'
html_use_index = True
html_title = 'CGNS Official Web Site'
html_static_path = ['_static']
html_sidebars={
    '**':['searchbox.html','localtoc.html'],
}
html_theme_options = {
    'touch_icon': 'images/logo/CGNS_empty.svg',
    'project_nav_name': 'CGNS doc test',
}    

# --- last line
