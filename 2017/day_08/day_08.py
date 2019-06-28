'''
aj dec -520 if icd < 9
z dec -500 if b <= 2
zz dec 628 if z >= 499
db dec -818 if u >= 0
zmq inc -787 if fhy <= -7
icd dec 770 if z <= 502
ykm dec -317 if uol == 8
u dec 940 if u != 0
'''

from collections import defaultdict

commands = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
}


triggers = defaultdict(int)
max_t = 0
max_abs = 0

for line in open('data.txt'):
    line = line.strip().split(' ')
    mul = 1 if line[1] == 'inc' else -1
    if commands[line[5]](triggers[line[4]], int(line[6])):
        triggers[line[0]] += mul * int(line[2])
    max_abs = max(*triggers.values(), max_abs)
max_t = max(triggers.values())

print(max_t, max_abs)