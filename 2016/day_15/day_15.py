import re
from collections import namedtuple

nt_disk = namedtuple('nt_disk', ('num', 'pos', 'init'))
disks = list(map(lambda x: nt_disk(x[0], x[1], x[3]), [list(map(int, re.findall(r'(\d+)', r))) for r in open('data.txt')]))

if 'part2':
    disks.append(nt_disk(len(disks)+1, 11, 0))

i = 0
while True:
    if any((d.init + d.num + i) % d.pos for d in disks):
        i += 1
    else:
        print('Result: %s' % i)
        break
