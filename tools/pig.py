import re
import sys
from collections import namedtuple

cmd_a = namedtuple("SED_A", "s, a") # append
cmd_s = namedtuple("SED_S", "s, r") # replace
cmd_t = namedtuple("SED_T", "s, p, a") # conditional

class convert:
    def __init__(self):
        self.cmd_list = []
        self.range_map = {}
        self.src = ""
        self.out = []
        self.idx = 0
        self.len = 0

    def set_text(self, text):
        self.src = text
        self.out = []
        self.idx = 0
        self.len = len(text)

    def compile(self, cmd_list):
        self.cmd_list = []
        for x in cmd_list:
            if isinstance(x, cmd_a):
                self.cmd_list.append(cmd_a(re.compile(x.s), x.a))
            elif isinstance(x, cmd_s):
                self.cmd_list.append(cmd_s(re.compile(x.s), x.r))
            elif isinstance(x, cmd_t):
                self.cmd_list.append(cmd_t(re.compile(x.s), re.compile(x.p), x.a))

    def run(self, cmd_list, text):
        self.compile(cmd_list)
        self.set_text(text)
        while self.idx < self.len:
            found = False
            text = self.src[self.idx:]
            for x in self.cmd_list:
                if isinstance(x, cmd_a):
                    m = x.s.match(text)
                    if m is not None:
                        matched_text = text[m.start(0):m.end(0)]
                        self.out.append(matched_text)
                        self.out.append(x.a)
                        self.idx += len(matched_text)
                        found = True
                        break
                elif isinstance(x, cmd_s):
                    m = x.s.match(text)
                    if m is not None:
                        matched_text = text[m.start(0):m.end(0)]
                        self.out.append(x.r)
                        self.idx += len(matched_text)
                        found = True
                        break
                elif isinstance(x, cmd_t):
                    if x.s not in self.range_map:
                        m = x.s.match(text)
                        if m is not None:
                            self.range_map[x.s] = (self.idx, self.len)
                    if x.s in self.range_map and self.range_map[x.s][0] <= self.idx < self.range_map[x.s][1]:
                        m = x.p.match(text)
                        if m is not None:
                            matched_text = text[m.start(0):m.end(0)]
                            self.out.append(x.a)
                            self.idx += len(matched_text)
                            found = True
                            break
            if not found:
                self.out.append(text[0])
                self.idx += 1
        return "".join(self.out)

def convert_bibtex():
    c = convert()
    cmd_list = [
        cmd_a('#include "cpascal.h"', '\n#include <setjmp.h> \njmp_buf jmp9998, jmp32; int lab31=0;'),
        cmd_a('#include "u*ptexdir/kanji.h"', '\n#include <setjmp.h> \njmp_buf jmp9998, jmp32; int lab31=0;'),
        cmd_s('goto lab31 ; *', '{lab31=1; return;}'),
        cmd_s('goto lab32', 'longjmp(jmp32,1)'),
        cmd_s('goto lab9998', 'longjmp(jmp9998,1)'),
        cmd_s('lab31:', ''),
        cmd_s('lab32:', ''),
        cmd_s('hack0 [(][)] ;', 'if(setjmp(jmp9998)==1) goto lab9998;'),
        cmd_s('hack1 [(][)] ;', 'if(setjmp(jmp32)==0)for(;;)'),
        cmd_s('hack2 [(][)]', 'break'),
        cmd_t('^void mainbody', r"while \( true", "while (lab31==0")
    ]
    data = ""
    for line in sys.stdin:
        data += line
    d = c.run(cmd_list, data)
    print(d)

def convert_mf1():
    data = ""
    for line in sys.stdin:
        data += line
    d0, _ = re.subn(r"\.\n", "\n.", data)
    d1, _ = re.subn(r"(\.hh|\.lh)", r"\1field", d0)
    print(d1)

def convert_mf2():
    data = ""
    for line in sys.stdin:
        data += line
    d0, _ = re.subn(r"else write", "else\nwrite", data)
    d1, _ = re.subn(r" (maxcoef *[^( ]|b1|b2|b3)", r" l\1", d0)
    print(d1)

def convert_pmp(src):
    cmd_list = [
        r"mpxout\.h",
        r"mpmp\.h",
        r"mplib\.h",
        r"mpstrings\.h",
        r"mpmath\.h",
        r"mpmathdouble\.h",
        r"mpmathdecimal\.h",
        r"mpmathbinary\.h",
        r"mplibps\.h",
        r"mppsout\.h",
        r"mplibpng\.h",
        r"mppngout\.h",
        r"mplibsvg\.h",
        r"mpsvgout\.h",
    ]
    data = read_data(src)
    ret, _ = re.subn(r"(%s)" % r"|".join(cmd_list), r"p\1", data)
    out = "p" + src.split("\\")[-1]
    with open(out, "w") as out_file:
        out_file.write(ret)

def read_data(name):
    data = ""
    with open(name, "r") as src:
        data = src.read()
    return data

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2 or sys.argv[1] not in ["run_cvtbib", "run_cvtmf1", "run_cvtmf2", "pmp"]:
        print("usage: pig.py <run_cvtbib|run_cvtmf1|run_cvtmf2|pmp>")
    else:
        task = sys.argv[1]
        if task == "run_cvtbib":
            convert_bibtex()
        elif task == "run_cvtmf1":
            convert_mf1()
        elif task == "run_cvtmf2":
            convert_mf2()
        elif task == "pmp":
            convert_pmp(sys.argv[2])
