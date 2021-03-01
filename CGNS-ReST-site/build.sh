#!/bin/sh

# CGNS Documentation files
#
# See https://poinot.github.io/cgns-test.github.io/governance/support.html
# for support in producing this doc
#
# See LICENSING/COPYRIGHT at root dir of this documentation sources
# this is doc generation for a UNIX host
# generation is made in a separate directory, change its path here:

export build_dir=../../cgns-test.github.io

cp -r ./images ${build_dir}/

sphinx-build -E -n -c . -b html source ${build_dir}

# last line






