from collections import defaultdict
from itertools import permutations
import sys

data = list(s.strip() for s in open('data.txt'))
for r in data:
    print(r)

def is_node(c):
    if c in '.#':
        return False
    return c

def is_wall(c):
    if c == '#':
        return True
    return False

def find_zero(lab):
    for x, row in enumerate(lab):
        if '0' in row:
            return (x, row.index('0'))

def find_costs(lab):
    nodes = {}
    for i, r in enumerate(lab):
        for j, c in enumerate(r):
            if is_node(c):
                nodes[c] = (i, j)

    costs = defaultdict(lambda: sys.maxsize)
    for node, (x, y) in nodes.items():
        print("Running %s" % node)
        walks = [(x, y)]
        step = 0
        visited = set()
        while walks:
            new_walks = []
            for (_x, _y) in walks:
                visited.add((_x, _y))
                wn = is_node(lab[_x][_y])
                if wn and wn != node:
                    key = tuple(sorted((wn, node)))
                    costs[key] = min(costs[key], step)
                for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                    nx, ny = dx+_x, dy+_y
                    if not is_wall(lab[nx][ny]) and (nx, ny) not in visited:

                        new_walks.append((nx, ny))
            step += 1
            walks = list(set(new_walks))

    print('calculating costs')
    mcost = sys.maxsize
    p2cost = sys.maxsize
    for p in permutations(nodes.keys()):
        if p[0] != '0':
            continue
        path = list(zip(p[:-1], p[1:]))
        cost = sum(costs[tuple(sorted(c))] for c in path)
        mcost = min(mcost, cost)
        p2cost = min(p2cost, cost + costs[('0', path[-1][-1])])

    print(mcost)
    print(p2cost)

find_costs(data)
