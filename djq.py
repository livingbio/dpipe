#!/usr/bin/env python

import dio
import fileinput
import json
from itertools import product
import re

re_name = re.compile(r'\.([\w]+)(.*)')
re_index = re.compile(r'\.\[([\d]*):?([\d]*):?([\d]*)\](.*)')

def _slice(start, end, p):
    start = (start and int(start)) or None
    end = (end and int(end)) or None
    p = (p and int(p)) or 1

    return slice(start, end, p)


def jpath(path, obj):
    if not obj: return []
    if not path: return [obj]

    if re_name.match(path) and isinstance(obj, dict):
        part, last = re_name.findall(path)[0]
        return jpath(last, obj.get(part))

    elif re_index.match(path) and isinstance(obj, list):
        start, end, p, last = re_index.findall(path)[0]

        results = []
        for k in obj[_slice(start, end, p)]:
            results.extend(jpath(last, k))

        return results

    return []
#    print path, obj
#    raise


def parse_filter(filter):
    if filter == "$filename":
        return lambda i: [fileinput.filename()]
    elif filter == "$lineno":
        return lambda i: [fileinput.lineno()]
    elif filter == "$filelineno":
        return lambda i: [fileinput.filelineno()]
    else:
        return lambda i: jpath(filter, i)



def djq(filters):
#    print filters
    # filter as a,.name,$file, something like this
    filters = [parse_filter(k) for k in filters.split(',')]

    for iline in dio.io():
#        print iline
        # one line should be one json
        obj = json.loads(iline)

        vs = [k(obj) for k in filters]
        vs = [[k] if not isinstance(k, list) else [] if k == None else k for k in vs]

        for v in product(*vs):
            print (u','.join(map(unicode, v))).encode('utf8')

if __name__ == "__main__":
    dio.now('djq')
