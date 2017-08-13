#!/usr/bin/env python3

import gzip
import sys
import json
from subprocess import Popen, PIPE
from xml.dom.minidom import parse

fname = sys.argv[1]

def svg_dimension(fname):
    f = open(fname)
    if fname.endswith('gz'):
        f = gzip.open(fname)

    dom = parse(f)
    svg = dom.childNodes[0]

    width = svg.attributes['width'].value
    height = svg.attributes['height'].value

    return width, height

def call_inkscape(fname, param):
    args = ['inkscape', fname, param]
    p = Popen(args=args, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    assert p.returncode == 0

    return out.strip()

pw, ph = svg_dimension(fname)
ix = call_inkscape(fname, '--query-x')
iy = call_inkscape(fname, '--query-y')
iw = call_inkscape(fname, '--query-width')
ih = call_inkscape(fname, '--query-height')

data = dict(page=dict(width=float(pw), height=float(ph)),
            image=dict(x=float(ix), y=float(iy),
                       width=float(iw), height=float(ih)))

print(json.dumps(data))

