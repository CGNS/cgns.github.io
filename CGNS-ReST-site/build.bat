@ECHO OFF

REM CGNS Documentation files
REM
REM See https://poinot.github.io/cgns-test.github.io/governance/support.html
REM for support in producing this doc
REM
REM See LICENSING/COPYRIGHT at root dir of this documentation sources
REM this is doc generation for a MS-Windows host
REm use Anaconda python distribution
REM generation is made in a separate directory, change its path here:

set build_dir=docs\_build\html

xcopy /q /i /s /e /y ".\images" "%build_dir%\images"

sphinx-build -n -c . -b html source %build_dir%

REM last line

