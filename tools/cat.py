import sys

if __name__ == "__main__":
    argc = len(sys.argv)

    if argc > 2:
        src_list = []
        for x in sys.argv[1:]:
            with open(x, "r") as src:
                src_list.append(src.read())
        print("\n".join(src_list))
