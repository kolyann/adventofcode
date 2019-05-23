import re
import sys
from itertools import combinations, permutations


data = [(s.strip().strip('.').split(' ')) for s in open('data.txt')]

relations = {}
peoples = set()

for r in data:
    relations[(r[0], r[10])] = int(r[3]) * (1 if r[2]=='gain' else -1)
    peoples.update((r[0], r[10]))

if 'part2':
    for ppl in peoples:
        relations[('You', ppl)] = 0
        relations[(ppl, 'You')] = 0
    peoples.update(('You',))


def get_sit_sum(order):
    cost = 0
    pairs = list(zip(order[:-1], order[1:])) + [(order[0], order[-1])]

    for p in pairs:
        cost += relations[p]
        cost += relations[p[::-1]]
    return cost

max_fun = 0
for pp in permutations(peoples):
    max_fun = max(max_fun, get_sit_sum(pp))

print(max_fun)