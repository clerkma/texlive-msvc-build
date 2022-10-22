# texlive-msvc-build

TeX Live with MSVC

## Requirements

* Visual Studio (tested 2019)
  * nmake
  * clang-cl (for libotfcc)
* Python 3 (tested 3.10.4)

## Supported Targets

* x86
* x64
* arm64 (except luajit related programs)

## Bootstrap

Prepare enviroment variables:

```bat
@rem set-var-x64.bat
set TLROOT=your\path\to\texlive
set TEXMFCNF=%TLROOT%\texk\kpathsea
set PREDEF=%CD%\predef
set TLTOOLS=%CD%\tools
set TLARCH=x64
@rem please make sure that directories existed
set TLBUILD=%CD%\x64-build
set TLWORKS=%CD%\bin\x64
@rem build xetex-specimen
set XETEXSP=your\path\to\xetex-specimen
set XETEXSPROOT=%XETEXSP%\xetexdir
set SPECIMENROOT=%XETEXSP%\libspecimen
```

Bootstrap:

```bat
tools\set-env-x64.bat
tools\make-libs.bat
nmake -nologo -f make\bootstrap.nmake
```

## `web2c` Programs

Build `web2c` programs:

```bat
nmake -nologo -f make\build.nmake all
```

To make an `exe` wrapper of `dll`-base engine/programs (eg. `xetex`):
```bat
cl -c -DDLLPROC=dllxetexmain call.c
link -out:xetex.exe call.obj %TLWORKS%\xetex.lib
```

Body of `call.c`:
```c
#include <stdio.h>

extern DLLPROC(int, char**);

int main(int ac, char ** av)
{
  return DLLPROC(ac, av);
}
```

To create symbolic links:
```bat
mklink xelatex.exe xetex.exe
mklink xelatex-dev.exe xetex.exe
```

## Lua*TeX

Build LuaTeX and LuaHBTeX:

```bat
nmake -nologo -f make\luatex.nmake luatex luahbtex
```

Build LuJITTeX and LuaJITHBTeX:

```bat
nmake -nologo -f make\luatex.nmake JIT=1 luajittex luajithbtex
```

## Supported Programs

* chktex
* cjkutils (bg5conv, cef5conv, cefconv, cefsconv, extconv, sjisconv, hbf2gf)
* detex
* dtl (dt2dv, dv2dt)
* dvi2tty (disdvi, dvi2tty)
* dvidvi
* dvipdfmx (exported `dlldvipdfmxmain`)
* dvips (afm2afm, dvips)
* kpsetools (kpseaccess, kpsestat, kpsewhich)
* makejvf
* makeindex
* mendex
* ttfdump


```bat
nmake -nologo -f make\build.nmake <prog_name>
```