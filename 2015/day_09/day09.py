import re
import sys
from itertools import combinations, permutations


data = [(s.strip().split(' ')) for s in open('test_data.txt')]

routes = {}
cities = set()

for r in data:
    routes[(r[0], r[2])] = int(r[4])
    routes[(r[2], r[0])] = int(r[4])
    cities.update((r[0], r[2]))

def get_route_sum(route):
    cost = 0
    pairs = zip(route[:-1], route[1:])
    for p in pairs:
        cost += routes[p]
    return cost

min_route = sys.maxsize
max_route = 0
for l in permutations(cities):
    min_route = min(min_route, get_route_sum(l))
    max_route = max(max_route, get_route_sum(l))

print(min_route, max_route)