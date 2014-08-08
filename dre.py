#!/usr/bin/env python
import dio
import re

def findall(pattern):
    for iline in dio.io():
#        print iline
        print ','.join(re.findall(pattern, iline)[0])

def sub(pattern, repl):
    for iline in dio.io():
        print re.sub(pattern, repl, iline)

if __name__ == "__main__":
    dio.now('findall')

