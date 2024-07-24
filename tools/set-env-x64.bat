@echo off
set VS22C="C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
set VS22B="C:\Program Files(x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
if exist %VS22C% (
    call %VS22C%
    exit /b 1
)
if exist %VS22B% (
    call %VS22B%
    exit /b 1
)
echo "I cannot found compiler. Please make sure that you have installed it."
@echo on
