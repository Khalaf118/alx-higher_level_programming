#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_no = len(sys.argv)
    result = 0
    if args_no == 1:
        print("0")
    else:
        for i in range(1, args_no):
            result = result + int(sys.argv[i])
        print("{}".format(result))
