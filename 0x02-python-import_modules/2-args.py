#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arglen = len(sys.argv) - 1
    if arglen == 0:
        print("0 arguments.".format())
    elif arglen == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arglen))
        for i in range(1, arglen + 1):
            print("{}: {}".format(i, sys.argv[i]))
