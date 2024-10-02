
call tools\make-libs.bat
nmake -nologo -f make\build.nmake all
call tools\make-exe-warpper.bat
