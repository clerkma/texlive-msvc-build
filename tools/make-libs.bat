for %%t in (cairo freetype gd gmp graphite2 harfbuzz icudata icuuc
    kpathsea luajit mpfr otfcc paper pixman png potrace pplib ptexenc runtime
    runtimep teckit texlua53 xpdf z zzip) do (
    nmake -f make\lib%%t.nmake
)