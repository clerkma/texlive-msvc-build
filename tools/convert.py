import fnmatch
import os
import sys

def read_source(arg):
    data = b""
    with open(arg, "rb") as src:
        data = src.read()
    return data

def combine_source(*args):
    source = []
    for x in args:
        source.append(read_source(x))
    return b"\n".join(source) + b"\n\n"

def get_path(name, default):
    p = os.getenv(name, default=default)
    return p.replace("\\", "/")

def convert(base):
    tl_root = get_path("TLROOT", default="texlive")
    src = f"{tl_root}/texk/web2c"
    tl_build_tool_root = get_path("TLTOOLS", default="tools")
    tl_build = get_path("TLBUILD", default="build")
    p_file = f"{base}.p"
    c_file = f"{base}.c"
    h_file = "cpascal.h"
    more_defines = []
    web2c_options = [f"-c{base}"]
    pre_cmd = ""
    mid_cmd = ""
    post_cmd = ""
    fixwrites_options = []
    splitup_options = "-i -l 65000"
    output = f"> {c_file}"

    tool_cat = f"{tl_build_tool_root}/cat.py"
    tool_dog = f"{tl_build_tool_root}/dog.py"
    tool_pig = f"{tl_build_tool_root}/pig.py"
    common_engine_list = [
        "mf", "mflua", "mfluajit", "tex", "aleph", "etex", "pdftex",
        "ptex", "eptex", "euptex", "uptex", "xetex"
    ]

    if base in ["pbibtex", "pdvitype", "ppltotf", "ptftopl"]:
        more_defines.append(f"{src}/ptexdir/ptex.defines")
        h_file = "ptexdir/kanji.h"
    elif base in ["upbibtex", "updvitype", "uppltotf", "uptftopl"]:
        more_defines.append(f"{src}/uptexdir/uptex.defines")
        h_file = "uptexdir/kanji.h"

    if base in ["bibtex", "pbibtex", "upbibtex"]:
        mid_cmd = f"py {tool_pig} run_cvtbib"
    elif base in common_engine_list:
        if fnmatch.fnmatch(base, "mf*"):
            more_defines = [
                f"{src}/web2c/texmf.defines",
                f"{src}/web2c/mfmp.defines",
            ]
            pre_cmd = f"py {tool_pig} run_cvtmf1"
            mid_cmd = f"py {tool_pig} run_cvtmf2"
            web2c_options = ["-m", f"-c{base}coerce"]
        else:
            more_defines = [
                f"{src}/web2c/texmf.defines",
                f"{src}/synctexdir/synctex.defines"
            ]
            web2c_options = ["-t", f"-c{base}coerce"]
            fixwrites_options = ["-t"]
        prog_defines = f"{src}/{base}dir/{base}.defines"
        if os.path.exists(prog_defines):
            more_defines.append(prog_defines)
        h_file = "texmfmp.h"
        post_cmd = f"splitup {splitup_options} {base}"
        c_file = f"{base}0.c"
        output = ""

    convert_bat_path = f"{tl_build}/convert-{base}.bat"
    with open(convert_bat_path, "w") as out:
        defs = [f"{src}/web2c/common.defines"] + more_defines
        cat_cmd = "py %s %s %s" % (tool_cat, " ".join(defs), p_file)
        opts = ["-h%s" % h_file] + web2c_options
        pipe_line = [
            cat_cmd,
            pre_cmd,
            "web2c %s" % (" ".join(opts)),
            mid_cmd,
            "fixwrites %s %s" % (" ".join(fixwrites_options), base),
            post_cmd
        ]
        out.write(make_pipe_line(pipe_line, output))
        if base in common_engine_list:
            out.write("\n")
            out.write(f"py {tool_dog} {base}coerce.h {src}/web2c/coerce.h")
            out.write("\n")
            out.write(f"makecpool {base} > {base}-pool.c")
    os.system(convert_bat_path)

def make_pipe_line(pipe_line, output):
    used_pipe_line = []
    for x in pipe_line:
        if x != "":
            used_pipe_line.append(x)
    used_pipe_line[-1] += output
    return " | ".join(used_pipe_line)

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print("usage: convert <program>")
    else:
        convert(sys.argv[1])
