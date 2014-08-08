#!/usr/bin/env python

from dpipe import dio
def _sort(key=None):
    lines = []
    for iline in dio.io():
        lines.append(iline.strip())

    if key:
        key = eval(key)

    lines.sort(key=key)
    for iline in lines:
        print iline


if __name__ == "__main__":
    dio.now('_sort')

