set VS22="C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
set VS19="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"
if exist %VS22% (
    call %VS22%
    exit /b 1
)
if exist %VS19% (
    call %VS19%
    exit /b 1
)
echo "I cannot found compiler. Please make sure that you have installed it."
