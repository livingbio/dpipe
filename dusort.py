#!/usr/bin/env python

import dio
from collections import defaultdict

def usort(key=None):
    if not key:
        container = set()
        add = lambda i: container.add(i)
        results = lambda: list(container)
    else:
        key = eval(key)
        container = {}
        add = lambda i: container.update({key(i): i})
        results = lambda: list(container.values())

    for iline in dio.io():
        iline = iline.strip()
        add(iline)

    r = results()
#    del container
    r.sort()

    for i in r:
        print i

if __name__ == "__main__":
    dio.now('usort')
