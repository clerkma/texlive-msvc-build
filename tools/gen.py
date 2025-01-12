
import os
import re

def run_build_icu_data():
    tlroot = os.getenv("TLROOT")
    tlbuild = os.getenv("TLBUILD")
    if tlroot is None or tlbuild is None:
        print("Please set variable 'TLROOT' and 'TLBUILD'. ")
    else:
        icudata_path = os.path.join(tlroot, r"libs\icu\icu-src\source\data\in")
        for x in os.listdir(icudata_path):
            m = re.fullmatch(r"icudt(?P<V>\d+)l\.dat", x)
            if m:
                name = x
                icudata_path = os.path.join(icudata_path, name)
                version = m.group(1)
                break
        icudata_data = None
        with open(icudata_path, "rb") as src:
            icudata_data = src.read()
        if icudata_data is None:
            print(f"'{name}': It seems empty.")
        else:
            out_name = os.path.join(tlbuild, "libicudata.c")
            with open(out_name, "w") as out:
                data_len = len(icudata_data)
                out.write("struct icudata {\n")
                out.write("  double item0;\n")
                out.write("  unsigned char item1[%d];\n" % data_len)
                out.write("} icudt%s_dat = { 0.0, {\n" % version)
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
    tlroot = os.getenv("TLROOT")
    predef = os.getenv("PREDEF")
    if tlroot is not None and predef is not None:
        name_src = task["file"].replace("$(TLROOT)", tlroot)
        name_out = task["out"].replace("$(PREDEF)", )
        with open(name_src) as src:
            text = src.read()
            for k, v in task["subs"].items():
                text = text.replace(k, v)
            with open(name_out, "w") as out:
                out.write(text)

if __name__ == "__main__":
    print("Generating ICU DATA ...")
    run_build_icu_data()
