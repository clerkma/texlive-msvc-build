import os, re

texlive_version = "TeX Live 2025/dev"
bibtex_x_config ="""\
/* config.h for bibtex-x */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define PACKAGE_VERSION "@VERSION"
#define TL_VERSION "@TL_VERSION"
#define PACKAGE_BUGREPORT "tex-k@tug.org"

#endif /* __CONFIG_H__ */
"""

cairo_public_src = """\
#ifdef _MSC_VER
#define cairo_public __declspec(dllexport)
#endif
"""
cairo_public_dst = """\
#if defined (_MSC_VER) && ! defined (CAIRO_WIN32_STATIC_BUILD)
#define cairo_public __declspec(dllimport)
#else
#define cairo_public
#endif
"""

chktex = """\
/* config.h for chktex */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define HAVE_STDARG_H 1
#define HAVE_VPRINTF 1
#define HAVE_LIMITS_H 1
#define HAVE_INTTYPES_H 1
#define HAVE_STDINT_H 1
#define HAVE_FILENO 1
#define HAVE_ISATTY 1
#define HAVE_STRLWR 1
#define HAVE_STRDUP 1
#define HAVE_STRCASECMP 1
#define HAVE_POSIX_ERE 1
#define TEX_LIVE 1

#define PACKAGE_VERSION "@VERSION"

#endif /* __CONFIG_H__ */
"""

detex = """\
/* c-auto.h for detex */
#ifndef __C_AUTO_H__
#define __C_AUTO_H__

#define HAVE_STRING_H 1
#define HAVE_LIMITS_H 1
#define YY_NO_UNISTD_H 1

#define VERSION "@VERSION"

#endif /* __C_AUTO_H__ */
"""

dtl = """\
/* config.h for dtl */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define TL_VERSION "@TL_VERSION"
#define PACKAGE_BUGREPORT "tex-k@tug.org"

#endif /* __CONFIG_H__ */
"""

dvi2tty = """\
/* c-auto.h for dvi2tty */
#ifndef __C_AUTO_H__
#define __C_AUTO_H__

#define VERSION "@VERSION"

#endif /* __C_AUTO_H__ */
"""

dvidvi = """\
/* config.h for dvidvi */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define VERSION "@VERSION"
#define TL_VERSION "@TL_VERSION"
#define PACKAGE_BUGREPORT "tex-k@tug.org"

#endif /* __CONFIG_H__ */
"""

dvipdfmx = """\
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define HAVE_GETENV 1
#define HAVE_INTTYPES_H 1
#define HAVE_LIBPNG 1
#define HAVE_STDINT_H 1
#define HAVE_SYS_TYPES_H 1
#define HAVE_SYS_WAIT_H 1
#define HAVE_TIMEZONE 1

#define HAVE_ZLIB 1
#define HAVE_ZLIB_COMPRESS2 1
#define HAVE_LIBPAPER 1

#define VERSION "@VERSION"

#endif /* __CONFIG_H__ */
"""

dvipng = """\
/* config.h for dvipng */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define HAVE_INTTYPES_H 1
#define HAVE_KPATHSEA_KPATHSEA_H 1
#define HAVE_FT2 1
#define HAVE_VPRINTF 1
#define HAVE_LIBKPATHSEA 1

#define HAVE_LIBPNG 1
#define HAVE_GDIMAGEGIF 1
#define HAVE_GDIMAGEPNGEX 1
#define HAVE_GDIMAGECREATETRUECOLOR 1
#define HAVE_GDIMAGECREATEFROMPNGPTR 1

#define PACKAGE_NAME "dvipng"
#define PACKAGE_VERSION "@VERSION"
#define PACKAGE_STRING "dvipng @VERSION"

#define GS_PATH "rungs"
#define HAVE_TEXLIVE_GS_INIT 1

#endif /* __CONFIG_H__ */
"""

dvips = """\
/* c-auto.h for dvips */
#ifndef __C_AUTO_H__
#define __C_AUTO_H__

#define VERSION "@VERSION"
#define TL_VERSION "@TL_VERSION"
#define PACKAGE_BUGREPORT "tex-k@tug.org"

#endif /* __C_AUTO_H__ */
"""

dvisvgm = """\
#ifndef VERSION_HPP
#define VERSION_HPP

constexpr const char *PROGRAM_NAME = "dvisvgm";
constexpr const char *PROGRAM_VERSION = "@VERSION";

#endif
"""

gmp = """\
#define HAVE_ALLOCA 1
#define HAVE_DOUBLE_IEEE_LITTLE_ENDIAN 1
#define HAVE_INTTYPES_H 1
#define HAVE_MEMSET 1
#define HAVE_RAISE 1
#define HAVE_STDINT_H 1
#define HAVE_STDIO_H 1
#define HAVE_STDLIB_H 1
#define HAVE_STRCHR 1
#define HAVE_STRING_H 1
#define HAVE_SYS_STAT_H 1
#define HAVE_SYS_TYPES_H 1

#define SIZEOF_MP_LIMB_T 8
#define SIZEOF_UNSIGNED 4
#define SIZEOF_UNSIGNED_LONG 4
#define SIZEOF_UNSIGNED_LONG_LONG 8
#define SIZEOF_UNSIGNED_SHORT 2

#ifdef _WIN64
#define SIZEOF_VOID_P 8
#else
#define SIZEOF_VOID_P 4
#endif

#define STDC_HEADERS 1

#define VERSION "@VERSION"

#define WANT_TMP_ALLOCA 1

#ifdef __cplusplus
#define inline __inline
#endif
"""

gregorio = """\
/* config_.h for gregorio */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#ifdef _MSC_VER
#define __attribute__(A)
#endif

#define HAVE_STDINT_H 1
#define ALIGNOF_UINT32_T __alignof(uint32_t)

#define VERSION "@VERSION"
#define PACKAGE_URL "http://gregorio-project.github.io/"

#endif /* __CONFIG_H__ */
"""

kpathsea = """\
#ifndef KPATHSEA_C_AUTO_H
#define KPATHSEA_C_AUTO_H

#define KPSEVERSION "kpathsea version @VERSION"

#define HAVE_ASSERT_H 1
#define HAVE_GETCWD 1
#define HAVE_INTTYPES_H 1
#define HAVE_LIMITS_H 1
#define HAVE_MEMCMP 1
#define HAVE_MEMCPY 1
#define HAVE_STDINT_H 1
#define HAVE_STDLIB_H 1
#define HAVE_STRCHR 1
#define HAVE_STRING_H 1
#define HAVE_STRRCHR 1
#define SIZEOF_LONG 4
#define STDC_HEADERS 1
#define HAVE_FLOAT_H 1
#define HAVE_UINTPTR_T 1

#define MAKE_OMEGA_OCP_BY_DEFAULT 1
#define MAKE_OMEGA_OFM_BY_DEFAULT 1
#define MAKE_TEX_FMT_BY_DEFAULT 1
#define MAKE_TEX_MF_BY_DEFAULT 1
#define MAKE_TEX_PK_BY_DEFAULT 1
#define MAKE_TEX_TEX_BY_DEFAULT 0
#define MAKE_TEX_TFM_BY_DEFAULT 1

#define MAKE_OMEGA_OCP_BY_DEFAULT 1
#define MAKE_OMEGA_OFM_BY_DEFAULT 1

#endif /* !KPATHSEA_C_AUTO_H */
"""

lcdf = """\
/* config.h for lcdf-typetools */
#ifndef __CONFIG_H__
#define __CONFIG_H__

#define HAVE_DECL_KPSE_OPENTYPE_FORMAT 1
#define HAVE_ADDRESSABLE_VA_LIST 1
#define HAVE_ADOBE_CODE 1
#define HAVE_AUTO_CFFTOT1 1
#define HAVE_AUTO_T1DOTLESSJ 1
#define HAVE_AUTO_TTFTOTYPE42 1
#define HAVE_STRERROR 1
#define HAVE_NEW_H 1
#define HAVE_INTTYPES_H 1
#define HAVE_PERMSTRING 1
#define HAVE_KPATHSEA 1

#define SIZEOF_LONG 4

#ifdef _WIN64
#define SIZEOF_VOID_P 8
#else
#define SIZEOF_VOID_P 4
#endif

#define HAVE_UINTPTR_T 1

#ifdef _MSC_VER
#include <BaseTsd.h>
typedef SSIZE_T ssize_t;
#endif

#define WORDS_BIGENDIAN 0
#define WORDS_BIGENDIAN_SET 1

#undef popen
#define popen win32_popen
#undef pclose
#define pclose win32_pclose

#ifdef __cplusplus
extern "C" {
#endif
#include <stdio.h>
extern FILE * win32_popen(const char *, const char *);
extern int win32_pclose(FILE *);
#ifdef __cplusplus
}
#endif

#define W_OK 2
#define F_OK 0
#define R_OK 4

#include <fcntl.h>

#define VERSION "@VERSION"
#define GLYPHLISTDIR ""
#define NOMINMAX 1 // for std::max

#ifdef PSRES 
#include <windows.h>
#endif

#define HAVE_DECL_KPSE_ENC_FORMAT 1
#define CDECL

#endif /* __CONFIG_H__ */
"""
makeindex = """\
/* c-auto.h for makeindex */
#ifndef __C_AUTO_H__
#define __C_AUTO_H__

#define TEX_LIVE_VERSION "@TL_VERSION"

#endif /* __C_AUTO_H__ */
"""
mendex = """\
/* c-auto.h for mendex */
#ifndef __C_AUTO_H__
#define __C_AUTO_H__

#define PACKAGE_VERSION "@VERSION"
#define TL_VERSION "@TL_VERSION"

#endif /* __C_AUTO_H__ */
"""

pat_ac = r"AC_INIT\(\[[^\]]*\],\s*\[(?P<VERSION>[^\]]*)\]"
pat_m4 = r"m4_define\(\[[^\]]*\],\s*\[(?P<VERSION>[^\]]*)\]"

def version(root, path, pattern):
    j = path_join(root, path)
    with open(j) as src:
        d = src.read()
        for x in re.finditer(pattern, d):
            return x.group(1)

def get_version(path, pattern):
    if os.path.exists(path):
        with open(path) as src:
            d = src.read()
            for x in re.finditer(pattern, d):
                return x.lastgroup, x.group(1)

def try_version(root, path):
    j = path_join(root, path)
    i = path_join(j, "version.ac")
    m = get_version(i, pat_m4)
    if m:
        return m
    i = path_join(j, "configure.ac")
    m = get_version(i, pat_m4)
    if m:
        return m
    m = get_version(i, pat_ac)
    if m:
        return m

def path_join(root, path):
    return os.path.normpath(os.path.join(root, path))

def make(root, path, template, output):
    j = path_join(root, path)
    text = template.replace("@TL_VERSION", texlive_version)
    m = try_version(root, path)
    if m:
        text = text.replace("@%s" % m[0], m[1])
    with open(output, "w") as out:
        out.write(text)

def copy(root, path, output, patch):
    j = path_join(root, path)
    if not patch:
        os.system('copy "%s" "%s"' % (j, output))
    else:
        text = ""
        with open(j) as src:
            text = src.read()
        for one in patch:
            src, dst = one
            text = text.replace(src, dst)
        with open(output, "w") as out:
            out.write(text)

root = os.getenv("TLROOT")

make(root,
    "texk/bibtex-x",
    bibtex_x_config,
    "predef/bibtex-x/config.h"
)
copy(root,
     "libs/cairo/cairo-src/src/cairoint.h",
     "predef/cairo/cairoint.h",
     [(cairo_public_src, cairo_public_dst)]
)
make(root,
     "texk/chktex",
     chktex,
     "predef/chktex/config.h"
)
make(root,
     "texk/detex",
     detex,
     "predef/detex/c-auto.h"
)
make(root,
     "texk/dtl",
     dtl,
     "predef/dtl/config.h"
)
make(root,
     "texk/dvi2tty",
     dvi2tty,
     "predef/dvi2tty/c-auto.h"
)
make(root,
     "texk/dvidvi",
     dvidvi,
    "predef/dvidvi/config.h"
)
make(root,
     "texk/dvipdfm-x",
     dvipdfmx,
    "predef/dvipdfmx/config.h"
)
make(root,
     "texk/dvipng",
     dvipng,
    "predef/dvipng/config.h"
)
make(root,
     "texk/dvipsk",
     dvips,
    "predef/dvips/c-auto.h"
)
make(root,
     "texk/dvisvgm",
     dvisvgm,
    "predef/dvisvgm/version.hpp"
)
make(root,
     "libs/gmp",
     gmp,
    "predef/gmp/config.h"
)
copy(root,
     "libs/gmp/gmp-src/gmp-h.in",
     "predef/gmp/gmp.h",
     [
        ("@HAVE_HOST_CPU_FAMILY_power@", "0"),
        ("@HAVE_HOST_CPU_FAMILY_powerpc@", "0"),
        ("@GMP_LIMB_BITS@", "64"),
        ("@GMP_NAIL_BITS@", "0"),
        ("@DEFN_LONG_LONG_LIMB@", "#define _LONG_LONG_LIMB 1"),
        ("@LIBGMP_DLL@", "0"),
        ("@CC@", "cl"),
        ("@CFLAGS@", "-DNO_ASM"),
    ]
)
make(root,
     "texk/gregorio",
     gregorio,
    "predef/gregorio/config_.h"
)

hb_version = version(root, "libs/harfbuzz/version.ac", pat_m4)
if hb_version:
    major, minor, micro = hb_version.split(".")
    copy(root,
         "libs/harfbuzz/harfbuzz-src/src/hb-version.h.in",
        "predef/harfbuzz/hb-version.h",
        [
            ("@HB_VERSION_MAJOR@", major),
            ("@HB_VERSION_MINOR@", minor),
            ("@HB_VERSION_MICRO@", micro),
            ("@HB_VERSION@", hb_version)
        ]
    )
make(root,
     "texk/kpathsea",
     kpathsea,
    "predef/kpathsea/c-auto.h"
)
make(root,
     "texk/lcdf-typetools",
     lcdf,
    "predef/lcdf-typetools/config.h"
)
copy(root,
     "libs/libpng/libpng-src/pnglibconf.h",
     "predef/libpng/pnglibconf.h", []
)
make(root,
     "texk/makeindex",
     makeindex,
    "predef/makeindex/c-auto.h"
)
make(root,
     "texk/mendexk",
     mendex,
    "predef/mendex/c-auto.h"
)
