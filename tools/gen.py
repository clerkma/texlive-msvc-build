
import os
import sys


gmp_h = {
    "file": "$(TLROOT)/libs/gmp/gmp-src/gmp-h.in",
    "out": "$(PREDEF)/gmp/gmp.h",
    "subs": {
        "@HAVE_HOST_CPU_FAMILY_power@": "0",
        "@HAVE_HOST_CPU_FAMILY_powerpc@": "0",
        "@GMP_LIMB_BITS@": "64",
        "@GMP_NAIL_BITS@": "0",
        "@DEFN_LONG_LONG_LIMB@": "#define _LONG_LONG_LIMB 1",
        "@LIBGMP_DLL@": "0",
        "@CC@": "cl",
        "@CFLAGS@": "-DNO_ASM",
    }
}


hb_version_h = {
    "file": "$(TLROOT)/libs/harfbuzz/harfbuzz-src/src/hb-version.h.in",
    "out": "$(PREDEF)/harfbuzz/hb-version.h",
    "subs": {
        "@HB_VERSION_MAJOR@": "5",
        "@HB_VERSION_MINOR@": "3",
        "@HB_VERSION_MICRO@": "0",
        "@HB_VERSION@": "5.3.0",
    }
}


pixman_version_h = {
    "file": "$(TLROOT)/libs/pixman/pixman-src/pixman/pixman-version.h.in",
    "out": "$(PREDEF)/pixman/pixman-version.h",
    "subs": {
        "@PIXMAN_VERSION_MAJOR@": "0",
        "@PIXMAN_VERSION_MINOR@": "40",
        "@PIXMAN_VERSION_MICRO@": "0",
    }
}


def run_build_icu_data():
    tlroot = os.getenv("TLROOT")
    tlbuild = os.getenv("TLBUILD")
    if tlroot is None or tlbuild is None:
        print("Please set variable 'TLROOT' and 'TLBUILD'. ")
    else:
        icudata_path = os.path.join(tlroot, r"libs\icu\icu-src\source\data\in\icudt71l.dat")
        icudata_data = None
        with open(icudata_path, "rb") as src:
            icudata_data = src.read()
        if icudata_data is None:
            print("'icudt71l.dat': It seems empty.")
        else:
            out_name = os.path.join(tlbuild, "libicudata.c")
            with open(out_name, "w") as out:
                data_len = len(icudata_data)
                out.write("struct icudata {\n")
                out.write("  double item0;\n")
                out.write("  unsigned char item1[%d];\n" % data_len)
                out.write("} icudt71_dat = { 0.0, {\n")
                row = (data_len + 15) // 16
                for i in range(row):
                    data = icudata_data[i*16:i*16+16]
                    out.write(", ".join(["0x%02X" % x for x in data]))
                    if row - 1 != i:
                        out.write(",\n")
                    else:
                        out.write("\n")
                out.write("}};")


def run(task):
    name_src = task["file"].replace("$(TLROOT)", os.getenv("TLROOT"))
    name_out = task["out"].replace("$(PREDEF)", os.getenv("PREDEF"))
    with open(name_src) as src:
        text = src.read()
        for k, v in task["subs"].items():
            text = text.replace(k, v)
        with open(name_out, "w") as out:
            out.write(text)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print("Usage: py <task>")
    else:
        if sys.argv[1] == "icudata":
            run_build_icu_data()
