#!/usr/bin/env python
#from dpipe import dio
import dio

if __name__ == "__main__":
    for iline in dio.io():
        print iline.strip().encode('utf8')
