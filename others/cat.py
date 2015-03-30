#! /usr/bin/python3.4

import fileinput

for line in fileinput.input():
    print(line,end="")
