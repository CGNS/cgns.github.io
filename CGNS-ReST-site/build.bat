REM CGNS Documentation files
REM See LICENSING/COPYRIGHT at root dir of this documentation sources

REM this is doc generation for a MS-Windows host
REm use Anaconda python distribution

@ECHO OFF

REM generation is made in a separate directory, change its path here:

set build_dir=..\..\cgns-test.github.io

xcopy /q /i /s /e /y ".\images" "%build_dir%\images"

sphinx-build -n -c . -b html source %build_dir%

REM last line

