#!/usr/bin/env python

from dpipe import dio
import sys, os
from collections import defaultdict
from collections import Counter
from itertools import product

def _join(key):
    files = [k for k in sys.argv[1:] if os.path.exists(k)]
    buffer = [defaultdict(list) for k in files]
    key = eval(key)

    for f, b in zip(files, buffer):
        with open(f) as ifile:
            for iline in ifile:
                iline = iline.strip()
                b[key(iline)].append(iline)

    c = Counter()
    for b in buffer:
        c.update(b.keys())
    
    for k in c:
        if c[k] == len(files):
            for v in product(*[b[k] for b in buffer]):
                print ','.join(v)
                

if __name__ == "__main__":
    dio.now("_join")
