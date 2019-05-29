import re
from collections import namedtuple
from pprint import pprint

disk_nt = namedtuple('disk_nt', ('x', 'y', 'size', 'used', 'avail'))

data = [disk_nt(*map(int, i[:-1])) for i in [re.findall(r'\d+', l) for l in open('data.txt').readlines()[2:]]]

table = [[0 for j in range(max(d.x for d in data)+1)] for i in range(max(d.y for d in data)+1)]


def print_table(table, l=5, symb=False):
    for r in table:
        for c in r:
            if symb:
                c = {1: 'O', 2: '.', 3: '#'}.get(len(c))
            print('{:{:}s}'.format(str(c), l), end='')
        print()

for d in data:
    table[d.y][d.x] = '{:}'.format(d.used)
print_table(table, l=1, symb=True)

sm = 0
for d in data:
    for k in data:
        if d != k and d.used != 0:
            if d.used < k.avail:
                sm += 1
print(sm)

print(69 + 31*5 + 1)