for %%t in (cairo freetype gd gmp graphite2 harfbuzz icudata icuio icui18n icuuc
    kpathsea luajit mpfi mpfr otfcc paper pixman png potrace pplib ptexenc runtime
    runtimep teckit texlua53 xpdf z zzip) do (
    nmake -nologo -f make\lib%%t.nmake
)