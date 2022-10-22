for %%t in (cairo freetype gmp graphite2 harfbuzz icudata icuuc
    kpathsea libgd libpaper luajit mpfr otfcc pixman png potrace pplib ptexenc runtime
    runtimep teckit texlua53 xpdf z zzip) do (
    nmake -f make\lib%%t.nmake
)