
nmake -nologo -f make\libkpathsea.nmake
nmake -nologo -f make\libruntime.nmake
nmake -nologo -f make\bootstrap.nmake
nmake -nologo -f make\build.nmake TLWORKS=%TLTOOLS%\bin tangleboot ctangleboot otangle tie

