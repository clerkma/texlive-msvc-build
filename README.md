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

```
@rem set-var-x64.bat
set TLROOT=your\path\to\texlive
set TEXMFCNF=%TLROOT%\texk\kpathsea
set PREDEF=%CD%\predef
set TLARCH=x64
@rem please make sure that directories existed
set TLBUILD=%CD%\x64-build
set TLWORKS=%CD%\bin\x64
set TLTOOLS=%CD%\tools
@rem build xetex-specimen
set XETEXSP=your\path\to\xetex-specimen
set XETEXSPROOT=%XETEXSP%\xetexdir
set SPECIMENROOT=%XETEXSP%\libspecimen
```

Bootstrap:

```
tools\set-env-x64.bat
make-libs.bat
nmake -nologo -f make\bootstrap.nmake
```

## `web2c` Programs

Build `web2c` programs:

```
nmake -nologo -f make\build.nmake all
```

## Lua*TeX

Build LuaTeX and LuaHBTeX:

```
nmake -nologo -f make\luatex.nmake luatex luahbtex
```

Build LuJITTeX and LuaJITHBTeX:

```
nmake -nologo -f make\luatex.nmake JIT=1 luajittex luajithbtex
```
