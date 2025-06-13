# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = ./docs/html
CURRENT_DIR   = $(shell pwd)

check_python:
	@python3 -c 'import sys; assert sys.version_info >= (3, 9), "Python 3.9+ is required"'

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(MAKE) check_python
	git submodule init
	git submodule update --init --force --remote
	if [ ! -d $(BUILDDIR) ]; then mkdir -p $(BUILDDIR); fi
	cp -r ./images "$(BUILDDIR)"
        cp -r .well-known "$(BUILDDIR)"
	@$(SPHINXBUILD) -E -n -c . -b html source "$(BUILDDIR)" $(SPHINXOPTS) $(O)

#@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
