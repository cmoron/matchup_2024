#!/usr/bin/env python3

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

countries = []
for l in lines[1:]:
    parts = l.split()
    name = parts[0]
    G, S, B = int(parts[1]), int(parts[2]), int(parts[3])
    countries.append((name, G, S, B))

sorted_countries = sorted(countries, key=lambda x: (-x[1], -x[2], -x[3]))
print(sorted_countries[0][0])
