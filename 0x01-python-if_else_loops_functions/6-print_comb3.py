#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i < j and i != 8:
            print("{:d}{:d}".format(i, j), end=", ")
        elif i < j and i == 8:
            print("{:d}{:d}".format(i, j))
