#!/bin/sh

# CGNS Documentation files
#
# See https://poinot.github.io/cgns-test.github.io/governance/support.html
# for support in producing this doc
#
# See LICENSING/COPYRIGHT at root dir of this documentation sources
# this is doc generation for a UNIX host
# generation is made in a separate directory, change its path here:

CURRENT_DIR=$PWD
cd ..
git submodule update --remote --merge
cd $CURRENT_DIR

export build_dir=./docs/_build/html

cp -r ./images ${build_dir}/

sphinx-build -E -n -c . -b html source ${build_dir}

# last line






