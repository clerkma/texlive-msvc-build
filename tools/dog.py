import sys

def read_src(a):
    data = ""
    with open(a) as src:
        data = src.read()
    return data


argc = len(sys.argv)

if argc == 3:
    src_list = []
    src = read_src(sys.argv[1])
    app = read_src(sys.argv[2])
    with open(sys.argv[1], "w") as out:
        out.write(src)
        out.write("\n")
        out.write(app)
