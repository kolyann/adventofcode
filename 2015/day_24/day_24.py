from itertools import combinations
from functools import reduce

def gen_perm(items, n):
    perms = []
    for i in range(1, len(items)+1):
        if perms:
            break
        combs = combinations(items, i)
        for combo in combs:
            if sum(combo) == n:
                perms.append(combo)
    return perms

def part(p):
    l = [int(l.strip()) for l in open('data.txt')]
    f = gen_perm(l, sum(l)/p)
    shortest_len = len(sorted(f, key=len)[0])
    min_qe = min(reduce(lambda a, b: a*b, x) for x in filter(lambda t: len(t)==shortest_len, f))
    return min_qe


print(part(4))
