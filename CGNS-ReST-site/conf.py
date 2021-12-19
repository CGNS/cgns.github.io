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
    'issue': ('https://cgnsorg.atlassian.net/projects/CGNS/issues/%s', '#'),
    'version': ('https://github.com/CGNS/CGNS/releases/tag/%s', 'version ')}

suppress_warnings = [ 'image.not_readable' ]

# --- sphinx code generation params
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['build']
pygments_style = 'sphinx'

# adding Lexer
from sphinx.highlighting import lexers
import sys
sys.path.append('.')
from sidslexer import SidsLexer

lexers["sids"] = SidsLexer()

import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
# CGNS is based on the guzzle theme
extensions.append("guzzle_sphinx_theme")
extensions.append('sphinx.ext.mathjax')
extensions.append('sphinxfortran.fortran_domain')
#extensions.append('breathe')

# --- Options for HTML output 
html_favicon =  'CGNS_empty.ico'
html_use_index = True
html_title = 'CGNS Official Web Site'
html_static_path = ['_static']
html_sidebars={
    '**':['searchbox.html','localtoc.html'],
}
html_theme_options = {
    'touch_icon': 'CGNS_empty.svg',
    'project_nav_name': 'CGNS doc test',
}    

html_css_files = [
    'css/filemap.css',
    'css/math_override.css'
]

## -- Breathe configuration ---
#
#import subprocess
#import os
#import shutil
#
## clone src with doxygen
#if os.path.exists("_breathe/CGNS"):
#   shutil.rmtree(os.path.join("_breathe","CGNS"))
#
#git_proc = subprocess.Popen(["git", "clone", "-b", "doxygen", "https://github.com/CGNS/CGNS.git", "_breathe/CGNS"])
#git_proc.communicate()
#
## Generate doxygen config file
#with open("_breathe/Doxyfile.in", "r") as f:
#    doxy_conf = f.read()
#doxy_conf = doxy_conf.replace("@CMAKE_CURRENT_SOURCE_DIR@", "./_breathe/CGNS")
#doxy_conf = doxy_conf.replace("@CMAKE_CURRENT_BINARY_DIR@", "./_breathe")
#with open("Doxyfile", "w") as f:
#    f.write(doxy_conf)
#
## Run doxygen
#run_doxygen =subprocess.Popen(["doxygen", "Doxyfile"])
#run_doxygen.communicate()
#
#breathe_projects = {
#        "CGNSMLLDoxygenBreathe": "_breathe/docs_mll/xml/"
#        }
#breathe_default_project = "CGNSMLLDoxygenBreathe"
#breathe_domain_by_extension = { "h" : "c" , "c" : "c"} 
#
## Clean up
#for dirpath, dirnames, filenames in os.walk(os.path.join("_breathe","CGNS")):
#    for dname in dirnames:
#        os.chmod(os.path.join(dirpath, dname), 0o775)
#    for fname in filenames:
#        os.chmod(os.path.join(dirpath, fname), 0o775)
#shutil.rmtree(os.path.join("_breathe","CGNS"))
##
# --- last line
