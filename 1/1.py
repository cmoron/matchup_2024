#!/usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

badges = []
for line in sys.stdin:
    badges.append(line.rstrip('\n'))

for badge in badges:
    if badge.startswith('42'):
        digits_sum = sum(int(digit) for digit in badge)
        if digits_sum == 75:
            print(badge)
            break
