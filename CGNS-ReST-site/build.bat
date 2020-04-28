@ECHO OFF

if not exist "build" mkdir build
cd build
if not exist "images" mkdir images
cd images
if not exist "logo" mkdir logo
cd ../..
copy images\logo\*.* build\images\logo
sphinx-build -n -c . -b html source build
