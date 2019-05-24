from collections import defaultdict, namedtuple
from copy import copy
from functools import reduce

data = open('data.txt')

class inv:
    def __init__(self):
        self.items = []

    def __add__(self, other):
        if not self.full:
            self.items.append(other)
        else:
            raise Exception("Can't add more")
        return True

    def add(self, item):
        self.__add__(item)

    @property
    def full(self):
        return len(self.items) == 2

    @property
    def pair(self):
        return sorted(self.items)

    def __repr__(self):
        return str(self.items)

    def clear(self):
        self.items = []

rules = defaultdict(dict)
state = defaultdict(inv)
outputs = defaultdict(list)


for line in data:
    line = line.strip()
    if line.startswith('value'):
        _, v, _, _, _, n = line.split(' ')
        state[int(n)] + int(v)
    if line.startswith('bot'):
        _, n, _, _, _, low, ln, _, _, _, high, hn = line.split()
        rules[int(n)] = ((low, int(ln)), (high, int(hn)))



bots = defaultdict(list)

while True:
    possibles = []
    for k, v in [(a, b) for a, b in state.items()]:
        if v.full:
            rule = rules[k]
            put = True
            for i in (0, 1):
                if rule[i][0] == 'bot' and state[rule[i][1]].full:
                    put = False
                    break
            if put:
                possibles.append(k)
    #print(possibles)
    if not possibles:
        break

    for pos in possibles:
        low, high = state[pos].pair
        bots[pos].append(low)
        bots[pos].append(high)
        rule = rules[pos]
        if rule[0][0] == 'bot':
            state[rule[0][1]] + low
        else:
            outputs[rule[0][1]].append(low)

        if rule[1][0] == 'bot':
            state[rule[1][1]] + high
        else:
            outputs[rule[0][1]].append(high)

        state[pos].clear()

a = 61
b = 17

print([(k, v) for k, v in bots.items() if a in v and b in v])

t = sum((outputs[0], outputs[1], outputs[2]), [])
print(reduce(lambda x, y: x*y, t))