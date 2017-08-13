#!/usr/bin/env python3

import sys
from xml.dom.minidom import parse

dom = parse(open(sys.argv[1]))
g = dom.getElementsByTagName('g')[0]

while True:
    c = g.childNodes[0]
    if c.tagName == 'path':
        break
    g.removeChild(c)

print(dom.toxml())

