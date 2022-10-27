import os
import sys


task_libkpathsea = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-DWIN32", "-DNO_KPSE_DLL", "-DMAKE_KPSE_DLL",
        "-I$(PREDEF)", "-I$(TLROOT)/texk"
    ],
    "root": "$(TLROOT)/texk/kpathsea",
    "components": [
        'tex-file.c', 'absolute.c', 'atou.c', 'cnf.c', 'concat.c',
        'concat3.c', 'concatn.c', 'db.c', 'debug.c', 'dir.c',
        'elt-dirs.c', 'expand.c', 'extend-fname.c', 'file-p.c',
        'find-suffix.c', 'fn.c', 'fontmap.c', 'getopt.c', 'getopt1.c',
        'hash.c', 'kdefault.c', 'kpathsea.c', 'line.c', 'magstep.c',
        'make-suffix.c', 'path-elt.c', 'pathsearch.c', 'proginit.c',
        'progname.c', 'readable.c', 'rm-suffix.c', 'str-list.c',
        'str-llist.c', 'tex-glyph.c', 'tex-hush.c', 'tex-make.c',
        'tilde.c', 'uppercasify.c', 'variable.c', 'version.c',
        'xbasename.c', 'xcalloc.c', 'xdirname.c', 'xfopen.c',
        'xfseek.c', 'xftell.c', 'xgetcwd.c', 'xmalloc.c',
        'xopendir.c', 'xputenv.c', 'xrealloc.c', 'xstat.c', 'xstrdup.c',
        'win32lib.c', 'knj.c'
    ],
    "out": "libkpathsea.lib",
    "prefix": "libkpathsea-",
}

task_ptexenc = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-DWIN32", "-DNO_KPSE_DLL", "-DNO_PTENC_DLL",
        "-I$(PREDEF)", "-I$(TLROOT)/texk", "-I$(TLROOT)/texk/ptexenc"
    ],
    "root": "$(TLROOT)/texk/ptexenc",
    "components": [
        'kanjicnv.c', 'ptexenc.c', 'unicode.c', 'unicode-jp.c' 
    ],
    "out": "libptexenc.lib",
    "prefix": "libptexenc-",
}

task_zlib = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-I$(TLROOT)/libs/zlib/zlib-src",
        "-I$(PREDEF)/zlib"
    ],
    "root": "$(TLROOT)/libs/zlib/zlib-src",
    "components": [
        "adler32.c", "compress.c", "crc32.c", "deflate.c",
        "infback.c", "gzclose.c", "gzlib.c", "gzread.c",
        "gzwrite.c", "inffast.c", "inflate.c", "inftrees.c",
        "trees.c", "uncompr.c", "zutil.c"
    ],
    "out": "libz.lib",
    "prefix": "libz-",
}

task_libpng = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-I$(PREDEF)/zlib",
        "-I$(TLROOT)/libs/zlib/zlib-src",
        "-I$(TLROOT)/libs/libpng/libpng-src",
        "-I$(PREDEF)/libpng"
    ],
    "root": "$(TLROOT)/libs/libpng/libpng-src",
    "components": [
        "png.c", "pngerror.c", "pngget.c", "pngmem.c", "pngpread.c",
        "pngread.c", "pngrio.c", "pngrtran.c", "pngrutil.c", "pngset.c",
        "pngtrans.c", "pngwio.c", "pngwrite.c", "pngwtran.c", "pngwutil.c",
    ],
    "out": "libpng.lib",
    "prefix": "libpng-",
}

task_libpaper = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-I$(PREDEF)/luatex", # unistd.h
        "-DPAPERSIZE=\\\"letter\\\"",
        "-DPAPERSIZEVAR=\\\"PAPERSIZE\\\"",
        "-D__STDC__", 
        "-Dstrcasecmp=_stricmp",
    ],
    "root": "$(TLROOT)/libs/libpaper/libpaper-src/lib",
    "components": [
        "dimen.c", "paper.c"
    ],
    "out": "libpaper.lib",
    "prefix": "libpaper-",
}

task_libfreetype = {
    "cflags": [
        "-nologo", "-c", "-utf-8", "-O2", "-Oy",
        "-DFT2_BUILD_LIBRARY",
        "-DDLG_API=\"\"",
        "-I$(TLROOT)/libs/freetype2/freetype-src/include",
    ],
    "root": "$(TLROOT)/libs/freetype2/freetype-src",
    "components": [
        "src/base/ftsystem.c", "src/base/ftdebug.c",
        "src/base/ftinit.c", "src/base/ftbase.c",
        "src/base/ftbbox.c", "src/base/ftbdf.c",
        "src/base/ftbitmap.c", "src/base/ftcid.c",
        "src/base/ftfstype.c", "src/base/ftgasp.c",
        "src/base/ftglyph.c", "src/base/ftgxval.c",
        "src/base/ftmm.c", "src/base/ftotval.c",
        "src/base/ftpatent.c", "src/base/ftpfr.c",
        "src/base/ftstroke.c", "src/base/ftsynth.c",
        "src/base/fttype1.c", "src/base/ftwinfnt.c",
        "src/truetype/truetype.c", "src/type1/type1.c",
        "src/cff/cff.c", "src/cid/type1cid.c", "src/pfr/pfr.c",
        "src/svg/svg.c",
        "src/type42/type42.c", "src/winfonts/winfnt.c",
        "src/pcf/pcf.c", "src/bdf/bdf.c", "src/sfnt/sfnt.c",
        "src/autofit/autofit.c", "src/pshinter/pshinter.c",
        "src/smooth/smooth.c", "src/raster/raster.c",
        "src/sdf/sdf.c", "src/cache/ftcache.c", "src/gzip/ftgzip.c",
        "src/lzw/ftlzw.c", "src/bzip2/ftbzip2.c", "src/psaux/psaux.c",
        "src/psnames/psnames.c", "src/dlg/dlg.c"
    ],
    "out": "libfreetype.lib",
    "prefix": "libfreetype-",
}

task_libgd = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-DBGDWIN32",
        "-DNONDLL",
        "-DHAVE_CONFIG_H",
        "-I$(PREDEF)/zlib",
        "-I$(PREDEF)/gd",
        "-I$(TLROOT)/libs/zlib/zlib-src",
        "-I$(TLROOT)/libs/libpng/libpng-src",
        "-I$(PREDEF)/libpng",
        "-I$(TLROOT)/libs/freetype2/freetype-src/include"
    ],
    "root": "$(TLROOT)/libs/gd/libgd-src",
    "components": [
        'src/gd.c', 'src/gd_avif.c', 'src/gd_bmp.c', 'src/gd_color.c',
        'src/gd_color_map.c', 'src/gd_color_match.c', 'src/gd_crop.c',
        'src/gd_filename.c', 'src/gd_filter.c', 'src/gd_gd.c',
        'src/gd_gd2.c', 'src/gd_gif_in.c', 'src/gd_gif_out.c',
        'src/gd_heif.c', 'src/gd_interpolation.c', 'src/gd_io.c',
        'src/gd_io_dp.c', 'src/gd_io_file.c', 'src/gd_io_ss.c',
        'src/gd_jpeg.c', 'src/gd_matrix.c', 'src/gd_nnquant.c',
        'src/gd_png.c', 'src/gd_rotate.c', 'src/gd_security.c',
        'src/gd_ss.c', 'src/gd_tga.c', 'src/gd_tiff.c', 'src/gd_topal.c',
        'src/gd_transform.c', 'src/gd_version.c', 'src/gd_wbmp.c',
        'src/gd_webp.c', 'src/gd_xbm.c', 'src/gdcache.c', 'src/gdfontg.c',
        'src/gdfontl.c', 'src/gdfontmb.c', 'src/gdfonts.c', 'src/gdfontt.c',
        'src/gdft.c', 'src/gdfx.c', 'src/gdhelpers.c', 'src/gdkanji.c',
        'src/gdtables.c', 'src/gdxpm.c', 'src/wbmp.c'
    ],
    "out": "libgd.lib",
    "prefix": "libgd-",
}

task_libpixman = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DPACKAGE=pixman",
        "-I$(TLROOT)/libs/pixman/pixman-src",
        "-I$(PREDEF)/pixman"
    ],
    "root": "$(TLROOT)/libs/pixman/pixman-src",
    "components": [
        'pixman/pixman.c', 'pixman/pixman-access.c',
        'pixman/pixman-access-accessors.c', 'pixman/pixman-bits-image.c',
        'pixman/pixman-combine32.c', 'pixman/pixman-combine-float.c',
        'pixman/pixman-conical-gradient.c', 'pixman/pixman-x86.c',
        'pixman/pixman-mips.c', 'pixman/pixman-arm.c',
        'pixman/pixman-ppc.c', 'pixman/pixman-edge.c',
        'pixman/pixman-edge-accessors.c', 'pixman/pixman-fast-path.c',
        'pixman/pixman-filter.c', 'pixman/pixman-glyph.c',
        'pixman/pixman-general.c', 'pixman/pixman-gradient-walker.c',
        'pixman/pixman-image.c', 'pixman/pixman-implementation.c',
        'pixman/pixman-linear-gradient.c', 'pixman/pixman-matrix.c',
        'pixman/pixman-noop.c', 'pixman/pixman-radial-gradient.c',
        'pixman/pixman-region16.c', 'pixman/pixman-region32.c',
        'pixman/pixman-solid-fill.c', 'pixman/pixman-timer.c',
        'pixman/pixman-trap.c', 'pixman/pixman-utils.c'
    ],
    "out": "libpixman.lib",
    "prefix": "libpixman-",
}

task_libgmp = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DHAVE_CONFIG_H",
        "-DNO_ASM",
        "-I$(TLROOT)/libs/gmp/gmp-src",
        "-I$(TLROOT)/libs/gmp/gmp-src/mpn/generic",
        "-I$(PREDEF)/gmp"
    ],
    "root": "$(TLROOT)/libs/gmp/gmp-src",
    "components": [
        'assert.c', 'compat.c', 'errno.c', 'extract-dbl.c', 'invalid.c',
        'memory.c', 'mp_bpl.c', 'mp_clz_tab.c', 'mp_dv_tab.c', 'mp_get_fns.c',
        'mp_minv_tab.c', 'mp_set_fns.c', 'nextprime.c', 'primesieve.c',
        'tal-reent.c', 'version.c',
        # 'mp_bases.c', 'popcount.c',
        'mpn/generic/add.c', 'mpn/generic/add_1.c', 'mpn/generic/add_n.c',
        'mpn/generic/addmul_1.c', 'mpn/generic/bdiv_dbm1c.c',
        'mpn/generic/bdiv_q.c', 'mpn/generic/bdiv_q_1.c',
        'mpn/generic/binvert.c', 'mpn/generic/cmp.c', 'mpn/generic/com.c',
        'mpn/generic/compute_powtab.c', 'mpn/generic/copyd.c',
        'mpn/generic/copyi.c', 'mpn/generic/dcpi1_bdiv_q.c',
        'mpn/generic/dcpi1_bdiv_qr.c', 'mpn/generic/dcpi1_div_q.c',
        'mpn/generic/dcpi1_div_qr.c', 'mpn/generic/dcpi1_divappr_q.c',
        'mpn/generic/div_q.c', 'mpn/generic/div_qr_2n_pi1.c',
        'mpn/generic/dive_1.c', 'mpn/generic/divexact.c',
        'mpn/generic/divrem.c', 'mpn/generic/divrem_1.c',
        'mpn/generic/divrem_2.c', 'mpn/generic/gcd_subdiv_step.c',
        'mpn/generic/gcdext.c', 'mpn/generic/gcdext_1.c',
        'mpn/generic/gcdext_lehmer.c', 'mpn/generic/get_str.c',
        'mpn/generic/hgcd.c', 'mpn/generic/hgcd2.c',
        'mpn/generic/hgcd_appr.c', 'mpn/generic/hgcd_matrix.c',
        'mpn/generic/hgcd_reduce.c', 'mpn/generic/hgcd_step.c',
        'mpn/generic/invertappr.c', 'mpn/generic/lshift.c',
        'mpn/generic/lshiftc.c', 'mpn/generic/matrix22_mul.c',
        'mpn/generic/matrix22_mul1_inverse_vector.c',
        'mpn/generic/mu_bdiv_q.c', 'mpn/generic/mu_div_q.c',
        'mpn/generic/mu_div_qr.c', 'mpn/generic/mu_divappr_q.c',
        'mpn/generic/mul.c', 'mpn/generic/mul_1.c',
        'mpn/generic/mul_basecase.c', 'mpn/generic/mul_fft.c',
        'mpn/generic/mul_n.c', 'mpn/generic/mullo_basecase.c',
        'mpn/generic/mullo_n.c', 'mpn/generic/mulmod_bnm1.c',
        'mpn/generic/neg.c', 'mpn/generic/nussbaumer_mul.c',
        'mpn/generic/powlo.c', 'mpn/generic/powm.c',
        'mpn/generic/pre_divrem_1.c', 'mpn/generic/redc_1.c',
        'mpn/generic/redc_n.c', 'mpn/generic/rshift.c',
        'mpn/generic/sbpi1_bdiv_q.c', 'mpn/generic/sbpi1_bdiv_qr.c',
        'mpn/generic/sbpi1_div_q.c', 'mpn/generic/sbpi1_div_qr.c',
        'mpn/generic/sbpi1_divappr_q.c', 'mpn/generic/scan1.c',
        'mpn/generic/set_str.c', 'mpn/generic/sqr.c',
        'mpn/generic/sqr_basecase.c', 'mpn/generic/sqrlo.c',
        'mpn/generic/sqrlo_basecase.c', 'mpn/generic/sqrmod_bnm1.c',
        'mpn/generic/sqrtrem.c', 'mpn/generic/sub.c',
        'mpn/generic/sub_1.c', 'mpn/generic/sub_n.c',
        'mpn/generic/submul_1.c', 'mpn/generic/tdiv_qr.c',
        'mpn/generic/toom22_mul.c', 'mpn/generic/toom2_sqr.c',
        'mpn/generic/toom32_mul.c', 'mpn/generic/toom33_mul.c',
        'mpn/generic/toom3_sqr.c', 'mpn/generic/toom42_mul.c',
        'mpn/generic/toom42_mulmid.c', 'mpn/generic/toom43_mul.c',
        'mpn/generic/toom44_mul.c', 'mpn/generic/toom4_sqr.c',
        'mpn/generic/toom53_mul.c', 'mpn/generic/toom63_mul.c',
        'mpn/generic/toom6_sqr.c', 'mpn/generic/toom6h_mul.c',
        'mpn/generic/toom8_sqr.c', 'mpn/generic/toom8h_mul.c',
        'mpn/generic/toom_couple_handling.c',
        'mpn/generic/toom_eval_dgr3_pm1.c',
        'mpn/generic/toom_eval_dgr3_pm2.c',
        'mpn/generic/toom_eval_pm1.c', 'mpn/generic/toom_eval_pm2.c',
        'mpn/generic/toom_eval_pm2exp.c', 'mpn/generic/toom_eval_pm2rexp.c',
        'mpn/generic/toom_interpolate_12pts.c',
        'mpn/generic/toom_interpolate_16pts.c',
        'mpn/generic/toom_interpolate_5pts.c',
        'mpn/generic/toom_interpolate_6pts.c',
        'mpn/generic/toom_interpolate_7pts.c',
        'mpn/generic/toom_interpolate_8pts.c',
        'mpn/generic/zero_p.c',
        'mpz/abs.c', 'mpz/add.c',
        'mpz/add_ui.c', 'mpz/aorsmul.c', 'mpz/aorsmul_i.c',
        'mpz/cfdiv_q_2exp.c', 'mpz/clear.c', 'mpz/cmp.c',
        'mpz/cmp_ui.c', 'mpz/cmpabs.c', 'mpz/divexact.c',
        'mpz/fdiv_q.c', 'mpz/fdiv_q_ui.c', 'mpz/fdiv_qr.c',
        'mpz/fits_slong.c', 'mpz/gcdext.c', 'mpz/get_si.c',
        'mpz/get_ui.c', 'mpz/init.c', 'mpz/init2.c', 'mpz/invert.c',
        'mpz/iset.c', 'mpz/iset_ui.c', 'mpz/mod.c', 'mpz/mul.c',
        'mpz/mul_2exp.c', 'mpz/mul_si.c', 'mpz/mul_ui.c', 'mpz/n_pow_ui.c',
        'mpz/neg.c', 'mpz/powm.c', 'mpz/powm_ui.c', 'mpz/realloc.c',
        'mpz/realloc2.c', 'mpz/scan0.c', 'mpz/scan1.c', 'mpz/set.c',
        'mpz/set_si.c', 'mpz/size.c', 'mpz/set_ui.c', 'mpz/sizeinbase.c',
        'mpz/sqrt.c', 'mpz/sub.c', 'mpz/sub_ui.c', 'mpz/swap.c',
        'mpz/tdiv_q.c', 'mpz/tdiv_q_2exp.c', 'mpz/tdiv_qr.c',
        'mpz/tdiv_r.c', 'mpz/tdiv_r_2exp.c', 'mpz/tstbit.c',
        'mpz/ui_pow_ui.c'
    ],
    "out": "libgmp.lib",
    "prefix": "libgmp-",
    "replace": {
        "mpn/generic/": "mpn-generic-",
        "mpz/": "mpz-",
    },
    "precmd": [
        r"$(TLTOOLS)\bin\gmp-gen-bases header 64 0 > $(PREDEF)\gmp\mp_bases.h",
        r"$(TLTOOLS)\bin\gmp-gen-fac 64 0 > $(PREDEF)\gmp\fac_table.h",
        r"$(TLTOOLS)\bin\gmp-gen-fib header 64 0 > $(PREDEF)\gmp\fib_table.h",
        r"$(TLTOOLS)\bin\gmp-gen-bases table 64 0 > $(TLBUILD)\mp_bases.c",
        r"$(CC) $(CFLAGS) -Fo$(TLBUILD)\libgmp-mp_bases.obj $(TLBUILD)\mp_bases.c",
        r"if exist $(TLBUILD)\popcount.c (del $(TLBUILD)\popcount.c)",
        r'echo #define OPERATION_popcount 1 >> $(TLBUILD)\popcount.c',
        r'echo #include ^<popham.c^> >> $(TLBUILD)\popcount.c',
        r"$(CC) $(CFLAGS) -Fo$(TLBUILD)\libgmp-popcount.obj $(TLBUILD)\popcount.c",
    ],
    "postcmd": [
        r"del $(PREDEF)\gmp\mp_bases.h",
        r"del $(PREDEF)\gmp\fac_table.h",
        r"del $(PREDEF)\gmp\fib_table.h",
        r"del $(TLBUILD)\mp_bases.c",
        r"del $(TLBUILD)\popcount.c",
    ]
}

task_libmpfr = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DHAVE_CONFIG_H",
        "-I$(TLROOT)/libs/mpfr/mpfr-src/src",
        "-I$(PREDEF)/gmp",
        "-I$(PREDEF)/mpfr",
    ],
    "root": "$(TLROOT)/libs/mpfr/mpfr-src",
    "components": [
        'src/abort_prec_max.c', 'src/add.c', 'src/add1.c',
        'src/add1sp.c', 'src/add_d.c', 'src/add_ui.c', 'src/agm.c',
        'src/atan.c', 'src/atan2.c', 'src/cache.c', 'src/clear.c',
        'src/clears.c', 'src/cmp.c', 'src/cmp2.c', 'src/cmpabs.c',
        'src/cmp_si.c', 'src/cmp_ui.c', 'src/comparisons.c',
        'src/const_catalan.c', 'src/const_euler.c', 'src/const_log2.c',
        'src/const_pi.c', 'src/constant.c', 'src/cos.c', 'src/div.c',
        'src/div_2si.c', 'src/div_2ui.c', 'src/div_ui.c',
        'src/exceptions.c', 'src/exp.c', 'src/exp2.c', 'src/exp3.c',
        'src/exp_2.c', 'src/extract.c', 'src/fits_sint.c',
        'src/fits_slong.c', 'src/fits_ulong.c', 'src/free_cache.c',
        'src/get_d.c', 'src/get_si.c', 'src/get_str.c', 'src/get_z.c',
        'src/get_z_exp.c', 'src/get_ui.c', 'src/gmp_op.c', 'src/init.c',
        'src/init2.c', 'src/inits2.c', 'src/isinteger.c', 'src/isnum.c',
        'src/isqrt.c', 'src/log.c', 'src/log2.c', 'src/min_prec.c',
        'src/mpfr-gmp.c', 'src/mpn_exp.c', 'src/mp_clz_tab.c', 'src/mul.c',
        'src/mul_2si.c', 'src/mul_2ui.c', 'src/mul_ui.c', 'src/mulders.c',
        'src/nbits_ulong.c', 'src/neg.c', 'src/next.c', 'src/pool.c',
        'src/powerof2.c', 'src/rem1.c', 'src/rint.c', 'src/round_near_x.c',
        'src/round_p.c', 'src/round_prec.c', 'src/scale2.c', 'src/set.c',
        'src/set_d.c', 'src/set_dfl_prec.c', 'src/set_f.c', 'src/set_prec.c',
        'src/set_q.c', 'src/set_rnd.c', 'src/set_si.c', 'src/set_si_2exp.c', 'src/set_str.c',
        'src/set_ui_2exp.c', 'src/set_ui.c', 'src/int_ceil_log2.c', 'src/set_z.c', 'src/set_z_exp.c',
        'src/set_zero.c', 'src/setmax.c', 'src/setmin.c', 'src/sgn.c',
        'src/sin.c', 'src/sin_cos.c', 'src/si_op.c', 'src/sqr.c',
        'src/sqrt.c', 'src/sqrt_ui.c', 'src/strtofr.c', 'src/sub.c',
        'src/sub1.c', 'src/sub1sp.c', 'src/sub_ui.c', 'src/swap.c',
        'src/ubf.c', 'src/ui_div.c', 'src/ui_sub.c', 'src/version.c'
    ],
    "out": "libmpfr.lib",
    "prefix": "libmpfr-",
    "replace": {
        "src/": "",
    },
    "precmd": [
        r"copy $(TLROOT)\libs\mpfr\mpfr-src\src\mparam_h.in $(PREDEF)\mpfr\mparam.h",
    ],
    "postcmd": [
        r"del $(PREDEF)\mpfr\mparam.h",
    ]
}

task_libcairo = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DCAIRO_WIN32_STATIC_BUILD", "-DCAIRO_NO_MUTEX", "-DPIXMAN_API=\"\"",
        "-I$(PREDEF)/cairo",
        "-I$(PREDEF)/cairo/src",
        "-I$(PREDEF)/pixman",
        "-I$(TLROOT)/libs/pixman/pixman-src/pixman",
        "-I$(PREDEF)/zlib",
        "-I$(TLROOT)/libs/zlib/zlib-src",
    ],
    "root": "$(PREDEF)/cairo/src",
    "components": [
        'cairo-analysis-surface.c', 'cairo-arc.c', 'cairo-array.c', 'cairo-atomic.c', 'cairo-base64-stream.c',
        'cairo-base85-stream.c', 'cairo-bentley-ottmann.c', 'cairo-bentley-ottmann-rectangular.c',
        'cairo-bentley-ottmann-rectilinear.c', 'cairo-botor-scan-converter.c', 'cairo-boxes.c', 'cairo-boxes-intersect.c',
        'cairo.c', 'cairo-cache.c', 'cairo-clip.c', 'cairo-clip-boxes.c', 'cairo-clip-polygon.c', 'cairo-clip-region.c',
        'cairo-clip-surface.c', 'cairo-color.c', 'cairo-composite-rectangles.c', 'cairo-compositor.c', 'cairo-contour.c',
        'cairo-damage.c', 'cairo-debug.c', 'cairo-default-context.c', 'cairo-device.c', 'cairo-error.c', 'cairo-fallback-compositor.c',
        'cairo-fixed.c', 'cairo-font-face.c', 'cairo-font-face-twin.c', 'cairo-font-face-twin-data.c', 'cairo-font-options.c',
        'cairo-freelist.c', 'cairo-freed-pool.c', 'cairo-gstate.c', 'cairo-hash.c', 'cairo-hull.c', 'cairo-image-compositor.c',
        'cairo-image-info.c', 'cairo-image-source.c', 'cairo-image-surface.c', 'cairo-line.c', 'cairo-lzw.c', 'cairo-matrix.c',
        'cairo-mask-compositor.c', 'cairo-mesh-pattern-rasterizer.c', 'cairo-mempool.c', 'cairo-misc.c', 'cairo-mono-scan-converter.c',
        'cairo-mutex.c', 'cairo-no-compositor.c', 'cairo-observer.c', 'cairo-output-stream.c', 'cairo-paginated-surface.c',
        'cairo-path-bounds.c', 'cairo-path.c', 'cairo-path-fill.c', 'cairo-path-fixed.c', 'cairo-path-in-fill.c', 'cairo-path-stroke.c',
        'cairo-path-stroke-boxes.c', 'cairo-path-stroke-polygon.c', 'cairo-path-stroke-traps.c', 'cairo-path-stroke-tristrip.c',
        'cairo-pattern.c', 'cairo-pdf-interchange.c', 'cairo-pen.c', 'cairo-polygon.c', 'cairo-polygon-intersect.c', 'cairo-polygon-reduce.c',
        'cairo-raster-source-pattern.c', 'cairo-recording-surface.c', 'cairo-rectangle.c', 'cairo-rectangular-scan-converter.c', 'cairo-region.c',
        'cairo-rtree.c', 'cairo-scaled-font.c', 'cairo-shape-mask-compositor.c', 'cairo-slope.c', 'cairo-spans.c', 'cairo-spans-compositor.c',
        'cairo-spline.c', 'cairo-stroke-dash.c', 'cairo-stroke-style.c', 'cairo-surface.c', 'cairo-surface-clipper.c', 'cairo-surface-fallback.c',
        'cairo-surface-observer.c', 'cairo-surface-offset.c', 'cairo-surface-snapshot.c', 'cairo-surface-subsurface.c', 'cairo-surface-wrapper.c',
        'cairo-tag-attributes.c', 'cairo-tag-stack.c', 'cairo-time.c', 'cairo-tor-scan-converter.c', 'cairo-tor22-scan-converter.c',
        'cairo-clip-tor-scan-converter.c', 'cairo-toy-font-face.c', 'cairo-traps.c', 'cairo-tristrip.c', 'cairo-traps-compositor.c',
        'cairo-unicode.c', 'cairo-user-font.c', 'cairo-version.c', 'cairo-wideint.c', 'cairo-pdf-surface.c', 'cairo-pdf-operators.c',
        'cairo-pdf-shading.c', 'cairo-cff-subset.c', 'cairo-scaled-font-subsets.c', 'cairo-truetype-subset.c', 'cairo-type1-fallback.c',
        'cairo-type1-glyph-names.c', 'cairo-type1-subset.c', 'cairo-type3-glyph-surface.c', 'cairo-deflate-stream.c'
    ],
    "out": "libcairo.lib",
    "prefix": "libcairo-",
    "precmd": [
        r"if exist $(PREDEF)\cairo\src (rd /S /Q $(PREDEF)\cairo\src)",
        r"md $(PREDEF)\cairo\src",
        r"copy $(TLROOT)\libs\cairo\cairo-src\src\*.c $(PREDEF)\cairo\src\ ",
        r"copy $(TLROOT)\libs\cairo\cairo-src\src\*.h $(PREDEF)\cairo\src\ ",
        r"copy $(TLROOT)\libs\cairo\cairo-src\cairo-version.h $(PREDEF)\cairo\cairo-version.h",
        r"del $(PREDEF)\cairo\src\cairoint.h",
    ],
    "postcmd": [
        r"rd /S /Q $(PREDEF)\cairo\src",
        r"if exist $(PREDEF)\cairo\cairo-version.h (del $(PREDEF)\cairo\cairo-version.h)"
    ]
}

task_libxpdf = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DHAVE_CONFIG_H",
        "-DPDF_PARSER_ONLY",
        "-I$(PREDEF)/xpdf",
        "-I$(TLROOT)/libs/xpdf/xpdf-src",
        "-I$(TLROOT)/libs/xpdf/xpdf-src/goo",
        "-I$(TLROOT)/libs/xpdf/xpdf-src/fofi",
        "-I$(TLROOT)/libs/xpdf/xpdf-src/splash",
    ],
    "root": "$(TLROOT)/libs/xpdf/xpdf-src",
    "components": [
        'goo/FixedPoint.cc', 'goo/GHash.cc', 'goo/GList.cc',
        'goo/GString.cc', 'goo/Trace.cc', 'goo/gfile.cc',
        'goo/gmem.cc', 'goo/gmempp.cc', 'fofi/FoFiBase.cc',
        'fofi/FoFiEncodings.cc', 'fofi/FoFiIdentifier.cc',
        'fofi/FoFiTrueType.cc', 'fofi/FoFiType1.cc',
        'fofi/FoFiType1C.cc', 'xpdf/AcroForm.cc', 'xpdf/Annot.cc',
        'xpdf/Array.cc', 'xpdf/BuiltinFont.cc', 'xpdf/BuiltinFontTables.cc',
        'xpdf/CMap.cc', 'xpdf/Catalog.cc', 'xpdf/CharCodeToUnicode.cc',
        'xpdf/Decrypt.cc', 'xpdf/Dict.cc', 'xpdf/Error.cc',
        'xpdf/FontEncodingTables.cc', 'xpdf/Function.cc',
        'xpdf/Gfx.cc', 'xpdf/GfxFont.cc', 'xpdf/GfxState.cc',
        'xpdf/GlobalParams.cc', 'xpdf/JArithmeticDecoder.cc',
        'xpdf/JBIG2Stream.cc', 'xpdf/JPXStream.cc', 'xpdf/Lexer.cc',
        'xpdf/Link.cc', 'xpdf/NameToCharCode.cc', 'xpdf/Object.cc',
        'xpdf/OptionalContent.cc', 'xpdf/Outline.cc', 'xpdf/OutputDev.cc',
        'xpdf/PDF417Barcode.cc', 'xpdf/PDFDoc.cc', 'xpdf/PDFDocEncoding.cc',
        'xpdf/PSTokenizer.cc', 'xpdf/Page.cc', 'xpdf/Parser.cc',
        'xpdf/SecurityHandler.cc', 'xpdf/Stream.cc', 'xpdf/TextString.cc',
        'xpdf/UnicodeMap.cc', 'xpdf/UnicodeRemapping.cc', 'xpdf/UTF8.cc',
        'xpdf/XFAScanner.cc', 'xpdf/XRef.cc', 'xpdf/Zoox.cc'
    ],
    "out": "libxpdf.lib",
    "prefix": "libxpdf-",
}

task_libzzip = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-I$(TLROOT)/libs/zziplib/zziplib-src",
        "-I$(TLROOT)/libs/zlib/zlib-src",
        "-I$(PREDEF)/zziplib",
        "-I$(PREDEF)/zlib"
    ],
    "root": "$(TLROOT)/libs/zziplib/zziplib-src/zzip",
    "components": [
        'dir.c', 'err.c', 'fetch.c', 'file.c',
        'info.c', 'plugin.c', 'stat.c', 'write.c',
        'zip.c'
    ],
    "out": "libzzip.lib",
    "prefix": "libzzip-",
}

task_libgraphite2 = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DGRAPHITE2_STATIC",
        "-DGRAPHITE2_NTRACING",
        "-I$(TLROOT)/libs/graphite2/graphite2-src/include",
        "-I$(TLROOT)/libs/freetype2/freetype2-src/include",
    ],
    "root": "$(TLROOT)/libs/graphite2/graphite2-src/src",
    "components": [
        'CmapCache.cpp', 'Code.cpp', 'Collider.cpp',
        'Decompressor.cpp', 'Face.cpp', 'FeatureMap.cpp',
        'Font.cpp', 'GlyphCache.cpp', 'GlyphFace.cpp',
        'Intervals.cpp', 'Justifier.cpp', 'NameTable.cpp',
        'Pass.cpp', 'Position.cpp', 'Segment.cpp',
        'Silf.cpp', 'Slot.cpp', 'Sparse.cpp',
        'TtfUtil.cpp', 'UtfCodec.cpp', 'gr_char_info.cpp',
        'gr_face.cpp', 'gr_features.cpp', 'gr_font.cpp',
        'gr_logging.cpp', 'gr_segment.cpp', 'gr_slot.cpp',
        'call_machine.cpp', 'FileFace.cpp'
    ],
    "out": "libgraphite2.lib",
    "prefix": "libgraphite2-",
}

task_libteckit = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-I$(TLROOT)/libs/teckit/TECkit-src/source/Public-headers",
        "-I$(TLROOT)/libs/zlib/zlib-src",
        "-I$(PREDEF)/zlib",
    ],
    "root": "$(TLROOT)/libs/teckit/TECkit-src/source",
    "components": [
        "Compiler.cpp",
        "UnicodeNames.cpp",
        "Sample-tools/TECkit_Compile.cpp",
        "Engine.cpp"
    ],
    "out": "libteckit.lib",
    "prefix": "libteckit-",
    "replace": {
        "Sample-tools/": "",
    }
}

task_libicuuc = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DU_IMPORT=", "-DU_EXPORT=",
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-DU_PLATFORM_USES_ONLY_WIN32_API=1",
        "-DU_COMMON_IMPLEMENTATION",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/common",
    "components": [
        'appendable.cpp', 'bmpset.cpp', 'brkeng.cpp', 'brkiter.cpp',
        'bytesinkutil.cpp', 'bytestream.cpp', 'bytestrie.cpp',
        'bytestriebuilder.cpp', 'bytestrieiterator.cpp', 'caniter.cpp',
        'characterproperties.cpp', 'chariter.cpp', 'charstr.cpp',
        'cmemory.cpp', 'cstr.cpp', 'cstring.cpp', 'cwchar.cpp',
        'dictbe.cpp', 'dictionarydata.cpp', 'dtintrv.cpp', 'edits.cpp',
        'emojiprops.cpp', 'errorcode.cpp', 'filteredbrk.cpp',
        'filterednormalizer2.cpp', 'icudataver.cpp', 'icuplug.cpp',
        'loadednormalizer2impl.cpp', 'localebuilder.cpp',
        'localematcher.cpp', 'localeprioritylist.cpp',
        'locavailable.cpp', 'locbased.cpp', 'locdispnames.cpp',
        'locdistance.cpp', 'locdspnm.cpp', 'locid.cpp', 'loclikely.cpp',
        'loclikelysubtags.cpp', 'locmap.cpp', 'locresdata.cpp',
        'locutil.cpp', 'lsr.cpp', 'lstmbe.cpp', 'messagepattern.cpp',
        'normalizer2.cpp', 'normalizer2impl.cpp', 'normlzr.cpp',
        'parsepos.cpp', 'patternprops.cpp', 'pluralmap.cpp', 'propname.cpp',
        'propsvec.cpp', 'punycode.cpp', 'putil.cpp', 'rbbi.cpp',
        'rbbi_cache.cpp', 'rbbidata.cpp', 'rbbinode.cpp', 'rbbirb.cpp',
        'rbbiscan.cpp', 'rbbisetb.cpp', 'rbbistbl.cpp', 'rbbitblb.cpp',
        'resbund.cpp', 'resbund_cnv.cpp', 'resource.cpp', 'restrace.cpp',
        'ruleiter.cpp', 'schriter.cpp', 'serv.cpp', 'servlk.cpp',
        'servlkf.cpp', 'servls.cpp', 'servnotf.cpp', 'servrbf.cpp',
        'servslkf.cpp', 'sharedobject.cpp', 'simpleformatter.cpp',
        'static_unicode_sets.cpp', 'stringpiece.cpp',
        'stringtriebuilder.cpp', 'uarrsort.cpp', 'ubidi.cpp',
        'ubidi_props.cpp', 'ubidiln.cpp', 'ubiditransform.cpp',
        'ubidiwrt.cpp', 'ubrk.cpp', 'ucase.cpp', 'ucasemap.cpp',
        'ucasemap_titlecase_brkiter.cpp', 'ucat.cpp', 'uchar.cpp',
        'ucharstrie.cpp', 'ucharstriebuilder.cpp', 'ucharstrieiterator.cpp',
        'uchriter.cpp', 'ucln_cmn.cpp', 'ucmndata.cpp', 'ucnv.cpp',
        'ucnv2022.cpp', 'ucnv_bld.cpp', 'ucnv_cb.cpp', 'ucnv_cnv.cpp',
        'ucnv_ct.cpp', 'ucnv_err.cpp', 'ucnv_ext.cpp', 'ucnv_io.cpp',
        'ucnv_lmb.cpp', 'ucnv_set.cpp', 'ucnv_u16.cpp', 'ucnv_u32.cpp',
        'ucnv_u7.cpp', 'ucnv_u8.cpp', 'ucnvbocu.cpp', 'ucnvdisp.cpp',
        'ucnvhz.cpp', 'ucnvisci.cpp', 'ucnvlat1.cpp', 'ucnvmbcs.cpp',
        'ucnvscsu.cpp', 'ucnvsel.cpp', 'ucol_swp.cpp', 'ucptrie.cpp',
        'ucurr.cpp', 'udata.cpp', 'udatamem.cpp', 'udataswp.cpp',
        'uenum.cpp', 'uhash.cpp', 'uhash_us.cpp', 'uidna.cpp', 'uinit.cpp',
        'uinvchar.cpp', 'uiter.cpp', 'ulist.cpp', 'uloc.cpp',
        'uloc_keytype.cpp', 'uloc_tag.cpp', 'umapfile.cpp', 'umath.cpp',
        'umutablecptrie.cpp', 'umutex.cpp', 'unames.cpp', 'unifiedcache.cpp',
        'unifilt.cpp', 'unifunct.cpp', 'uniset.cpp', 'uniset_closure.cpp',
        'uniset_props.cpp', 'unisetspan.cpp', 'unistr.cpp', 'unistr_case.cpp',
        'unistr_case_locale.cpp', 'unistr_cnv.cpp', 'unistr_props.cpp',
        'unistr_titlecase_brkiter.cpp', 'unorm.cpp', 'unormcmp.cpp',
        'uobject.cpp', 'uprops.cpp', 'ures_cnv.cpp', 'uresbund.cpp',
        'uresdata.cpp', 'usc_impl.cpp', 'uscript.cpp', 'uscript_props.cpp',
        'uset.cpp', 'uset_props.cpp', 'usetiter.cpp', 'ushape.cpp',
        'usprep.cpp', 'ustack.cpp', 'ustr_cnv.cpp',
        'ustr_titlecase_brkiter.cpp', 'ustr_wcs.cpp', 'ustrcase.cpp',
        'ustrcase_locale.cpp', 'ustrenum.cpp', 'ustrfmt.cpp',
        'ustring.cpp', 'ustrtrns.cpp', 'utext.cpp', 'utf_impl.cpp',
        'util.cpp', 'util_props.cpp', 'utrace.cpp', 'utrie.cpp',
        'utrie2.cpp', 'utrie2_builder.cpp', 'utrie_swap.cpp', 'uts46.cpp',
        'utypes.cpp', 'uvector.cpp', 'uvectr32.cpp', 'uvectr64.cpp',
        'wintz.cpp'
    ],
    "out": "libicuuc.lib",
    "prefix": "libicuuc-",
    "replace": {
    }
}

task_libicui18n = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-DU_I18N_IMPLEMENTATION",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/i18n",
    "components": [
        'alphaindex.cpp', 'anytrans.cpp', 'astro.cpp', 'basictz.cpp',
        'bocsu.cpp', 'brktrans.cpp', 'buddhcal.cpp', 'calendar.cpp',
        'casetrn.cpp', 'cecal.cpp', 'chnsecal.cpp', 'choicfmt.cpp',
        'coleitr.cpp', 'coll.cpp', 'collation.cpp', 'collationbuilder.cpp',
        'collationcompare.cpp', 'collationdata.cpp',
        'collationdatabuilder.cpp', 'collationdatareader.cpp',
        'collationdatawriter.cpp', 'collationfastlatin.cpp',
        'collationfastlatinbuilder.cpp', 'collationfcd.cpp',
        'collationiterator.cpp', 'collationkeys.cpp', 'collationroot.cpp',
        'collationrootelements.cpp', 'collationruleparser.cpp',
        'collationsets.cpp', 'collationsettings.cpp',
        'collationtailoring.cpp', 'collationweights.cpp',
        'compactdecimalformat.cpp', 'coptccal.cpp', 'cpdtrans.cpp',
        'csdetect.cpp', 'csmatch.cpp', 'csr2022.cpp', 'csrecog.cpp',
        'csrmbcs.cpp', 'csrsbcs.cpp', 'csrucode.cpp', 'csrutf8.cpp',
        'curramt.cpp', 'currfmt.cpp', 'currpinf.cpp', 'currunit.cpp',
        'dangical.cpp', 'datefmt.cpp', 'dayperiodrules.cpp',
        'dcfmtsym.cpp', 'decContext.cpp', 'decNumber.cpp', 'decimfmt.cpp',
        'double-conversion-bignum-dtoa.cpp', 'double-conversion-bignum.cpp',
        'double-conversion-cached-powers.cpp',
        'double-conversion-double-to-string.cpp',
        'double-conversion-fast-dtoa.cpp',
        'double-conversion-string-to-double.cpp',
        'double-conversion-strtod.cpp', 'dtfmtsym.cpp',
        'dtitvfmt.cpp', 'dtitvinf.cpp', 'dtptngen.cpp', 'dtrule.cpp',
        'erarules.cpp', 'esctrn.cpp', 'ethpccal.cpp', 'fmtable.cpp',
        'fmtable_cnv.cpp', 'format.cpp', 'formatted_string_builder.cpp',
        'formattedval_iterimpl.cpp', 'formattedval_sbimpl.cpp',
        'formattedvalue.cpp', 'fphdlimp.cpp', 'fpositer.cpp',
        'funcrepl.cpp', 'gender.cpp', 'gregocal.cpp', 'gregoimp.cpp',
        'hebrwcal.cpp', 'indiancal.cpp', 'inputext.cpp', 'islamcal.cpp',
        'japancal.cpp', 'listformatter.cpp', 'measfmt.cpp', 'measunit.cpp',
        'measunit_extra.cpp', 'measure.cpp', 'msgfmt.cpp', 'name2uni.cpp',
        'nfrs.cpp', 'nfrule.cpp', 'nfsubs.cpp', 'nortrans.cpp',
        'nultrans.cpp', 'number_affixutils.cpp', 'number_asformat.cpp',
        'number_capi.cpp', 'number_compact.cpp', 'number_currencysymbols.cpp',
        'number_decimalquantity.cpp', 'number_decimfmtprops.cpp',
        'number_fluent.cpp', 'number_formatimpl.cpp', 'number_grouping.cpp',
        'number_integerwidth.cpp', 'number_longnames.cpp',
        'number_mapper.cpp', 'number_modifiers.cpp', 'number_multiplier.cpp',
        'number_notation.cpp', 'number_output.cpp', 'number_padding.cpp',
        'number_patternmodifier.cpp', 'number_patternstring.cpp',
        'number_rounding.cpp', 'number_scientific.cpp',
        'number_skeletons.cpp', 'number_symbolswrapper.cpp',
        'number_usageprefs.cpp', 'number_utils.cpp', 'numfmt.cpp',
        'numparse_affixes.cpp', 'numparse_compositions.cpp',
        'numparse_currency.cpp', 'numparse_decimal.cpp',
        'numparse_impl.cpp', 'numparse_parsednumber.cpp',
        'numparse_scientific.cpp', 'numparse_symbols.cpp',
        'numparse_validators.cpp', 'numrange_capi.cpp',
        'numrange_fluent.cpp', 'numrange_impl.cpp', 'numsys.cpp',
        'olsontz.cpp', 'persncal.cpp', 'pluralranges.cpp', 'plurfmt.cpp',
        'plurrule.cpp', 'quant.cpp', 'quantityformatter.cpp', 'rbnf.cpp',
        'rbt.cpp', 'rbt_data.cpp', 'rbt_pars.cpp', 'rbt_rule.cpp',
        'rbt_set.cpp', 'rbtz.cpp', 'regexcmp.cpp', 'regeximp.cpp',
        'regexst.cpp', 'regextxt.cpp', 'region.cpp', 'reldatefmt.cpp',
        'reldtfmt.cpp', 'rematch.cpp', 'remtrans.cpp', 'repattrn.cpp',
        'rulebasedcollator.cpp', 'scientificnumberformatter.cpp',
        'scriptset.cpp', 'search.cpp', 'selfmt.cpp',
        'sharedbreakiterator.cpp', 'simpletz.cpp', 'smpdtfmt.cpp',
        'smpdtfst.cpp', 'sortkey.cpp', 'standardplural.cpp',
        'string_segment.cpp', 'strmatch.cpp', 'strrepl.cpp',
        'stsearch.cpp', 'taiwncal.cpp', 'timezone.cpp', 'titletrn.cpp',
        'tmunit.cpp', 'tmutamt.cpp', 'tmutfmt.cpp', 'tolowtrn.cpp',
        'toupptrn.cpp', 'translit.cpp', 'transreg.cpp', 'tridpars.cpp',
        'tzfmt.cpp', 'tzgnames.cpp', 'tznames.cpp', 'tznames_impl.cpp',
        'tzrule.cpp', 'tztrans.cpp', 'ucal.cpp', 'ucln_in.cpp',
        'ucol.cpp', 'ucol_res.cpp', 'ucol_sit.cpp', 'ucoleitr.cpp',
        'ucsdet.cpp', 'udat.cpp', 'udateintervalformat.cpp',
        'udatpg.cpp', 'ufieldpositer.cpp', 'uitercollationiterator.cpp',
        'ulistformatter.cpp', 'ulocdata.cpp', 'umsg.cpp', 'unesctrn.cpp',
        'uni2name.cpp', 'units_data.cpp', 'units_complexconverter.cpp',
        'units_converter.cpp', 'units_router.cpp', 'unum.cpp',
        'unumsys.cpp', 'upluralrules.cpp', 'uregex.cpp', 'uregexc.cpp',
        'uregion.cpp', 'usearch.cpp', 'uspoof.cpp', 'uspoof_build.cpp',
        'uspoof_conf.cpp', 'uspoof_impl.cpp', 'utf16collationiterator.cpp',
        'utf8collationiterator.cpp', 'utmscale.cpp', 'utrans.cpp',
        'vtzone.cpp', 'vzone.cpp', 'windtfmt.cpp', 'winnmfmt.cpp',
        'wintzimpl.cpp', 'zonemeta.cpp', 'zrule.cpp', 'ztrans.cpp'
    ],
    "out": "libicui18n.lib",
    "prefix": "libicui8n-",
}

task_libicuio = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_IO_IMPLEMENTATION",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
        "-I$(TLROOT)/libs/icu/icu-src/source/io",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/io",
    "components": [
        'locbund.cpp', 'sprintf.cpp', 'sscanf.cpp', 'ucln_io.cpp',
        'ufile.cpp', 'ufmt_cmn.cpp', 'uprintf.cpp', 'uprntf_p.cpp',
        'uscanf.cpp', 'uscanf_p.cpp', 'ustdio.cpp', 'ustream.cpp'
    ],
    "out": "libicuio.lib",
    "prefix": "libicuio-",
}

task_libicutu = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_TOOLUTIL_IMPLEMENTATION",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    "components": [
        'collationinfo.cpp', 'dbgutil.cpp', 'denseranges.cpp',
        'filestrm.cpp', 'filetools.cpp', 'flagparser.cpp',
        'package.cpp', 'pkg_genc.cpp', 'pkg_gencmn.cpp',
        'pkg_icu.cpp', 'pkgitems.cpp', 'ppucd.cpp', 'swapimpl.cpp',
        'toolutil.cpp', 'ucbuf.cpp', 'ucln_tu.cpp', 'ucm.cpp',
        'ucmstate.cpp', 'udbgutil.cpp', 'unewdata.cpp', 'uoptions.cpp',
        'uparse.cpp', 'writesrc.cpp', 'xmlparser.cpp'
    ],
    "out": "libicutu.lib",
    "prefix": "libicutu-",
}

task_libicudata = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/stubdata",
    "components": [
        'stubdata.cpp',
    ],
    "out": "libicudata.lib",
    "prefix": "libicudata-",
}

task_libicutest = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-DT_CTEST_IMPLEMENTATION",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/ctestfw",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/ctestfw",
    "components": [
        'uperf.cpp', 'ucln_ct.c', 'tstdtmod.cpp',
        'testdata.cpp', 'datamap.cpp', 'ctest.c',
    ],
    "out": "libicutest.lib",
    "prefix": "libicutest-",
}

task_icu_makeconv = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/makeconv",
    "components": [
        'ucnvstat.c', 'makeconv.cpp', 'genmbcs.cpp',
        'gencnvex.c',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "makeconv.exe",
    "prefix": "makeconv-",
}

task_icu_genrb = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
        "-I$(TLROOT)/libs/icu/icu-src/source/io",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/genrb",
    "components": [
        'errmsg.c', 'filterrb.cpp', 'genrb.cpp', 'parse.cpp', 'prscmnts.cpp', 'rbutil.c',
        'read.c', 'reslist.cpp', 'rle.c', 'ustr.c', 'wrtjava.cpp', 'wrtxml.cpp'
    ],
    "libs": [
        "libicuio.lib", "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "genrb.exe",
    "prefix": "genrb-",
}

task_icu_genbrk = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/genbrk",
    "components": [
        'genbrk.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "genbrk.exe",
    "prefix": "genbrk-",
}

task_icu_gencnval = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gencnval",
    "components": [
        'gencnval.c',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gencnval.exe",
    "prefix": "gencnval-",
}

task_icu_gensprep = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gensprep",
    "components": [
        'store.c', 'gensprep.c',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gensprep.exe",
    "prefix": "gensprep-",
}

task_icu_icuinfo = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/ctestfw",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/icuinfo",
    "components": [
        'icuinfo.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "icuinfo.exe",
    "prefix": "icuinfo-",
}

task_icu_genccode = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/genccode",
    "components": [
        'genccode.c',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "genccode.exe",
    "prefix": "genccode-",
}

task_icu_gencmn = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gencmn",
    "components": [
        'gencmn.c',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gencmn.exe",
    "prefix": "gencmn-",
}

task_icu_icupkg = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/icupkg",
    "components": [
        'icupkg.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "icupkg.exe",
    "prefix": "icupkg-",
}

task_icu_pkgdata = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/pkgdata",
    "components": [
        'pkgtypes.c', 'pkgdata.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "pkgdata.exe",
    "prefix": "pkgdata-",
}

task_icu_gentest = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/ctestfw",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gentest",
    "components": [
        'gentest.c', 'genres32.c',
    ],
    "libs": [
        "libicutest.lib", "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gentest.exe",
    "prefix": "gentest-",
}

task_icu_gennorm2 = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gennorm2",
    "components": [
        'norms.cpp', 'n2builder.cpp', "gennorm2.cpp", 'extradata.cpp'
    ],
    "libs": [
        "libicutest.lib", "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gennorm2.exe",
    "prefix": "gennorm2-",
}

task_icu_gencfu = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/i18n",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gencfu",
    "components": [
        'gencfu.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gencfu.exe",
    "prefix": "gencfu-",
}

task_icu_gendict = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/gendict",
    "components": [
        'gendict.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "gendict.exe",
    "prefix": "gendict-",
}

task_icu_icuexportdata = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/icuexportdata",
    "components": [
        'icuexportdata.cpp',
    ],
    "libs": [
        "libicutu.lib", "libicui18n.lib", "libicuuc.lib", "libicudata.lib",
    ],
    "syslibs": [
        "advapi32.lib",
    ],
    "out": "icuexportdata.exe",
    "prefix": "icuexportdata-",
}

task_icu_escapesrc = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-EHsc",
        "-DU_IMPORT=", "-DU_EXPORT=", 
        "-DU_ATTRIBUTE_DEPRECATED=",
        "-I$(TLROOT)/libs/icu/icu-src/source/common",
        "-I$(TLROOT)/libs/icu/icu-src/source/tools/toolutil",
    ],
    "root": "$(TLROOT)/libs/icu/icu-src/source/tools/escapesrc",
    "components": [
        'escapesrc.cpp',
    ],
    "libs": [
    ],
    "syslibs": [
    ],
    "out": "escapesrc.exe",
    "prefix": "secapesrc-",
}

task_libharfbuzz = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-I$(TLROOT)/libs/harfbuzz/harfbuzz-src/src"
        "-I$(TLROOT)/libs/freetype2/freetype2-src/include",
        "-I$(PREDEF)/harfbuzz",
        "-I$(TLROOT)/libs/graphite2/graphite2-src/include",
        "-DGRAPHITE2_STATIC",
        "-DHAVE_GRAPHITE2",
    ],
    "root": "$(TLROOT)/libs/harfbuzz/harfbuzz-src/src",
    "components": [
        'hb-blob.cc', 'hb-buffer-serialize.cc', 'hb-buffer-verify.cc', 'hb-buffer.cc', 'hb-common.cc',
        'hb-draw.cc', 'hb-face.cc', 'hb-font.cc', 'hb-map.cc', 'hb-number.cc', 'hb-ot-cff1-table.cc',
        'hb-ot-cff2-table.cc', 'hb-ot-face.cc', 'hb-ot-name.cc', 'hb-ot-tag.cc', 'hb-set.cc', 'hb-shape.cc',
        'hb-shape-plan.cc', 'hb-shaper.cc', 'hb-static.cc', 'hb-style.cc', 'hb-subset-cff-common.cc', 'hb-subset-cff1.cc',
        'hb-subset-cff2.cc', 'hb-ucd.cc', 'hb-unicode.cc', 'hb-fallback-shape.cc', 'hb-aat-layout.cc',
        'hb-aat-map.cc', 'hb-ot-font.cc', 'hb-ot-layout.cc', 'hb-ot-color.cc', 'hb-ot-map.cc', 'hb-ot-math.cc',
        'hb-ot-meta.cc', 'hb-ot-metrics.cc', 'hb-ot-shape.cc', 'hb-ot-shaper-arabic.cc', 'hb-ot-shaper-default.cc',
        'hb-ot-shaper-hangul.cc', 'hb-ot-shaper-hebrew.cc', 'hb-ot-shaper-indic-table.cc', 'hb-ot-shaper-indic.cc',
        'hb-ot-shaper-khmer.cc', 'hb-ot-shaper-myanmar.cc', 'hb-ot-shaper-syllabic.cc', 'hb-ot-shaper-thai.cc',
        'hb-ot-shaper-use.cc', 'hb-ot-shaper-vowel-constraints.cc', 'hb-ot-shape-normalize.cc', 'hb-ot-shape-fallback.cc',
        'hb-ot-var.cc', 'hb-graphite2.cc'
    ],
    "out": "libharfbuzz.lib",
    "prefix": "libharfbuzz-",
}

task_libruntime = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-I$(TLROOT)/texk/web2c/lib",
        "-I$(PREDEF)",
        "-I$(TLROOT)/texk",
    ],
    "root": "$(TLROOT)/texk/web2c/lib",
    "components": [
        "basechsuffix.c", "chartostring.c", "coredump.c", "eofeoln.c",
        "fprintreal.c", "inputint.c", "input2int.c", "main.c",
        "openclose.c", "printversion.c", "setupvar.c", "uexit.c",
        "usage.c", "version.c", "zround.c"
    ],
    "out": "libruntime.lib",
    "prefix": "libruntime-",
}

task_libruntimep = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy", "-DWIN32", "-DNO_KPSE_DLL", "-DNO_PTENC_DLL", "-DPTEX",
        "-I$(TLROOT)/texk/web2c/lib",
        "-I$(PREDEF)",
        "-I$(TLROOT)/texk",
        "-I$(TLROOT)/texk/ptexenc",
    ],
    "root": "$(TLROOT)/texk/web2c/lib",
    "components": [
        "basechsuffix.c", "chartostring.c", "coredump.c", "eofeoln.c",
        "fprintreal.c", "inputint.c", "input2int.c", "main.c",
        "openclose.c", "printversion.c", "setupvar.c", "uexit.c",
        "usage.c", "version.c", "zround.c"
    ],
    "out": "libruntimep.lib",
    "prefix": "libruntimep-",
    "replace": {
    }
}

task_libtexlua53 = {
    "cflags": [
        "-nologo", "-utf-8", "-c", "-O2", "-Oy",
        "-DLUA_COMPAT_MODULE",
        "-DLUA_COMPAT_5_2",
        "-DLUAI_HASHLIMIT=6",
        "-I$(TLROOT)/texk/web2c/lib",
        "-I$(PREDEF)",
        "-I$(TLROOT)/texk",
        "-I$(TLROOT)/texk/ptexenc",
    ],
    "root": "$(TLROOT)/libs/lua53/lua53-src/src",
    "components": [
        'lapi.c', 'lauxlib.c', 'lbaselib.c', 'lbitlib.c', 'lcode.c', 'lcorolib.c',
        'lctype.c', 'ldblib.c', 'ldebug.c', 'ldo.c', 'ldump.c', 'lfunc.c', 'lgc.c',
        'linit.c', 'liolib.c', 'llex.c', 'lmathlib.c', 'lmem.c', 'loadlib.c', 'lobject.c',
        'lopcodes.c', 'loslib.c', 'lparser.c', 'lstate.c', 'lstring.c', 'lstrlib.c', 'ltable.c',
        'ltablib.c', 'ltm.c', 'lua.c', 'lundump.c', 'lutf8lib.c', 'lvm.c', 'lzio.c'
    ],
    "out": "libtexlua53.lib",
    "prefix": "libtexlua53-",
    "replace": {
    }
}

task_libpplib = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-I$(TLROOT)/libs/pplib/pplib-src/src/util",
        "-I$(TLROOT)/libs/pplib/pplib-src/src",
        "-I$(PREDEF)/zlib",
        "-I$(TLROOT)/libs/zlib/zlib-src",
    ],
    "root": "$(TLROOT)/libs/pplib/pplib-src/src",
    "components": [
        "ppheap.c", "pparray.c", "ppdict.c", "ppstream.c", "ppcrypt.c", "ppxref.c", "ppload.c",
        "util/utilbasexx.c", "util/utilflate.c", "util/utillzw.c", "util/utilfpred.c",
        "util/utillog.c", "util/utilnumber.c", "util/utiliof.c", "util/utilmd5.c", "util/utilsha.c", "util/utilcrypt.c",
        "util/utilmem.c", "util/utilmemheap.c", "util/utilmemheapiof.c", "util/utilmeminfo.c"
    ],
    "out": "libpplib.lib",
    "prefix": "libpplib-",
    "replace": {
        "util/": "",
    }
}

task_potrace = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-DHAVE_INTTYPES_H",
        "-DVERSION=\\\"1.16\\\"",
        "-I$(TLROOT)/libs/potrace/potrace-src/src",
    ],
    "root": "$(TLROOT)/libs/potrace/potrace-src/src",
    "components": [
        "curve.c", "decompose.c", "potracelib.c", "trace.c"
    ],
    "out": "libpotrace.lib",
    "prefix": "libpotrace-",
}

task_otfcc = {
    "cflags": [
        "-nologo", "-c", "-O2", "-Oy",
        "-I$(TLROOT)/texk/kpathsea", # for getopt
        "-I$(TLROOT)/texk/web2c/mfluadir/otfcc/include",
        "-I$(TLROOT)/texk/web2c/mfluadir/otfcc/include/dep",
        "-I$(TLROOT)/texk/web2c/mfluadir/otfcc/lib",
        "-I$(PREDEF)/otfcc/polyfill-msvc",
        "-DMAKE_KPSE_DLL", # for getopt
        "-D_CRT_SECURE_NO_WARNINGS",
        "-D_CARYLL_USE_PRE_SERIALIZED",
        "-DMAIN_VER=0",
        "-DSECONDARY_VER=10",
        "-DPATCH_VER=4",
        "$(OTFCC_ARCH_CFLAGS)", # for arm64 --target=arm64-pc-windows-msvc
    ],
    "root": "$(TLROOT)/texk/web2c/mfluadir/otfcc",
    "components": [
        'dep/extern/emyg-dtoa/emyg-dtoa.c', 'dep/extern/json.c', 'dep/extern/json-builder.c',
        'dep/extern/sds.c', 'src/luafunc.c', 'src/otfccdll.c', 'lib/consolidate/consolidate.c',
        'lib/consolidate/otl/gsub-single.c', 'lib/consolidate/otl/gpos-single.c', 'lib/consolidate/otl/chaining.c',
        'lib/consolidate/otl/common.c', 'lib/consolidate/otl/gsub-multi.c', 'lib/consolidate/otl/gsub-reverse.c',
        'lib/consolidate/otl/gsub-ligature.c', 'lib/consolidate/otl/GDEF.c', 'lib/consolidate/otl/gpos-pair.c',
        'lib/consolidate/otl/gpos-cursive.c', 'lib/consolidate/otl/mark.c', 'lib/support/options.c',
        'lib/support/unicodeconv/unicodeconv.c', 'lib/support/handle.c', 'lib/support/buffer/buffer.c',
        'lib/support/primitives.c', 'lib/support/glyph-order.c', 'lib/support/sha1/sha1.c', 'lib/support/ttinstr/ttinstr.c',
        'lib/support/base64/base64.c', 'lib/support/json/json-ident.c', 'lib/support/aglfn/aglfn.c', 'lib/otf-writer/stat.c',
        'lib/otf-writer/otf-writer.c', 'lib/otf-reader/otf-reader.c', 'lib/otf-reader/unconsolidate.c', 'lib/vf/axis.c',
        'lib/vf/region.c', 'lib/vf/vq.c', 'lib/logger/logger.c', 'lib/bk/bkgraph.c', 'lib/bk/bkblock.c', 'lib/font/caryll-font.c',
        'lib/font/caryll-sfnt-builder.c', 'lib/font/caryll-sfnt.c', 'lib/json-writer/json-writer.c', 'lib/json-reader/json-reader.c',
        'lib/libcff/cff-string.c', 'lib/libcff/cff-opmean.c', 'lib/libcff/charstring-il.c', 'lib/libcff/cff-fdselect.c', 'lib/libcff/cff-parser.c',
        'lib/libcff/subr.c', 'lib/libcff/cff-charset.c', 'lib/libcff/cff-index.c', 'lib/libcff/cff-codecs.c', 'lib/libcff/cff-writer.c',
        'lib/libcff/cff-dict.c', 'lib/libcff/cff-value.c', 'lib/table/vhea.c', 'lib/table/fvar.c', 'lib/table/cmap.c', 'lib/table/meta/read.c',
        'lib/table/meta/type.c', 'lib/table/meta/build.c', 'lib/table/meta/parse.c', 'lib/table/meta/dump.c', 'lib/table/vdmx/type.c',
        'lib/table/vdmx/funcs.c', 'lib/table/hhea.c', 'lib/table/post.c', 'lib/table/cvt.c', 'lib/table/CFF.c', 'lib/table/gasp.c', 
        'lib/table/LTSH.c', 'lib/table/maxp.c', 'lib/table/COLR.c', 'lib/table/vmtx.c', 'lib/table/fpgm-prep.c', 'lib/table/head.c', 
        'lib/table/CPAL.c', 'lib/table/_TSI.c', 'lib/table/name.c', 'lib/table/OS_2.c', 'lib/table/hdmx.c', 'lib/table/glyf/read.c', 
        'lib/table/glyf/glyf.c', 'lib/table/glyf/build.c', 'lib/table/GDEF.c', 'lib/table/VORG.c', 'lib/table/otl/coverage.c', 
        'lib/table/otl/read.c', 'lib/table/otl/classdef.c', 'lib/table/otl/build.c', 'lib/table/otl/parse.c', 'lib/table/otl/dump.c', 
        'lib/table/otl/subtables/gsub-single.c', 'lib/table/otl/subtables/gpos-single.c', 'lib/table/otl/subtables/chaining/read.c', 
        'lib/table/otl/subtables/chaining/common.c', 'lib/table/otl/subtables/chaining/classifier.c', 'lib/table/otl/subtables/chaining/build.c', 
        'lib/table/otl/subtables/chaining/parse.c', 'lib/table/otl/subtables/chaining/dump.c', 'lib/table/otl/subtables/gpos-mark-to-ligature.c', 
        'lib/table/otl/subtables/gpos-mark-to-single.c', 'lib/table/otl/subtables/gsub-multi.c', 'lib/table/otl/subtables/gsub-reverse.c', 
        'lib/table/otl/subtables/gpos-common.c', 'lib/table/otl/subtables/gsub-ligature.c', 'lib/table/otl/subtables/extend.c', 
        'lib/table/otl/subtables/gpos-pair.c', 'lib/table/otl/subtables/gpos-cursive.c', 'lib/table/otl/otl.c', 'lib/table/otl/constants.c', 
        'lib/table/hmtx.c', 'lib/table/BASE.c', 'lib/table/SVG.c', 'lib/table/TSI5.c'
    ],
    "out": "libotfcc.lib",
    "prefix": "libotfcc-",
    "cc": "clang-cl",
    "replace": {
        "/": "-"
    }
}


def build(conf):
    cmd_list = []
    cflags = " ".join(conf["cflags"])
    if "precmd" in conf:
        for x in conf["precmd"]:
            cmd_list.append(x)
    for x in conf["components"]:
        y = x
        if "replace" in conf:
            for p, r in conf["replace"].items():
                y = y.replace(p, r)
        else:
            y = x.split("/")[-1]
        if y.split(".")[-1] == "cpp":
            object_name = "$(TLBUILD)\\" + conf["prefix"] + y.replace(".cpp", ".obj")
        elif y.split(".")[-1] == "cc":
            object_name = "$(TLBUILD)\\" + conf["prefix"] + y.replace(".cc", ".obj")
        else:
            object_name = "$(TLBUILD)\\" + conf["prefix"] + y.replace(".c", ".obj")
        cmd = "$(CC) $(CFLAGS) -Fo%s $(ROOT)\\%s" % (object_name, x.replace("/", "\\"))
        cmd_list.append(cmd)
    if ".lib" in conf["out"]:
        cmd = "lib -nologo -out:$(TLBUILD)\\%s $(TLBUILD)\\%s*.obj" % (conf["out"], conf["prefix"])
    else:
        libs = " ".join(["$(PREDEF)\\%s" % x for x in conf["libs"]])
        libs += " " + " ".join(conf["syslibs"])
        cmd = "link -nologo -out:$(PREDEF)\\%s $(TLBUILD)\\%s*.obj %s" % (conf["out"], conf["prefix"], libs)
    cmd_list.append(cmd.replace("/", "\\"))
    if "postcmd" in conf:
        for x in conf["postcmd"]:
            cmd_list.append(x)
    with open("%s.nmake" % conf["prefix"][:-1], "w") as out:
        if "cc" in conf:
            out.write("CC=%s\n" % conf["cc"])
        out.write("ROOT=%s\n" % conf["root"].replace("/", "\\"))
        out.write("CFLAGS=%s\n" % cflags.replace("/", "\\"))
        out.write("all:\n")
        out.write("\n".join(["\t%s" % x for x in cmd_list]))

def run_build_icu():
    build(task_libicudata)
    build(task_libicuuc)
    build(task_libicui18n)
    build(task_libicuio)


def run_build_icu_data():
    with open("libicudata.nmake", "w") as out:
        out.write("all:\n")
        out.write("\t$(CC) -nologo -c -Fo$(TLBUILD)\libicudata.obj $(TLBUILD)\\libicudata.c\n")
        out.write("\tlib -nologo -out:$(TLBUILD)\libicudata.lib $(TLBUILD)\libicudata.obj\n")


task_map = {
    "cairo": task_libcairo,
    "harfbuzz": task_libharfbuzz,
    "kpathsea": task_libkpathsea,
    "pixman": task_libpixman,
    "png": task_libpng,
    "ptexenc": task_ptexenc,
    "runtime": task_libruntime,
    "runtimep": task_libruntimep,
    "xpdf": task_libxpdf,
    "zlib": task_zlib,
    "mpfr": task_libmpfr,
    "gmp": task_libgmp,
    "texlua53": task_libtexlua53,
    "zzip": task_libzzip,
    "pplib": task_libpplib,
    "teckit": task_libteckit,
    "graphite2": task_libgraphite2,
    "freetype": task_libfreetype,
    "potrace": task_potrace,
    "gd": task_libgd,
    # "icudata": task_libicudata,
    "icuuc": task_libicuuc,
    "otfcc": task_otfcc,
    "paper": task_libpaper,
    "icuio": task_libicuio,
    "icui18n": task_libicui18n,
}

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print("Usage: build.py <task> ...")
    else:
        task = sys.argv[1:]
        if "all" in task:
            for k, v in task_map.items():
                build(v)
        else:
            for one in task:
                if one in task_map:
                    build(task_map[one])
                elif one == "icu":
                    run_build_icu()
                elif one == "icudata":
                    run_build_icu_data()

