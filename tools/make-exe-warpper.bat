FOR /r %TLWORKS% %%F IN (*.lib) DO  (
    cl -nologo -c -O2 -DDLLPROC=dll%%~nFmain -Fo%TLBUILD%\call-%%~nF.obj %TLROOT%\texk\texlive\windows_wrapper\calldll.c
    link -nologo -out:%TLWORKS%\%%~nF.exe %TLBUILD%\call-%%~nF.obj %%F
)