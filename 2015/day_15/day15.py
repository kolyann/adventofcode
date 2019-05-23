'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'

import sys
from itertools import product
import itertools
from itertools import combinations, permutations
import math



spicies = {}

for line in open('data.txt'):
    ingr = line.split(':')[0]
    spicies[ingr] = [int(x.strip().split(' ')[1]) for x in line.split(':')[1].split(',')][:-1]

taste_n = 4


def gsum(n, spice):
    max_sum = 0
    for i in product(*[range(n+1) for r in range(len(spice))]):
        if sum(i) == n and all(i):
            tastes = [0 for _ in range(taste_n)]
            cur_foods = [[k*n for k in sp] for (_,sp), n in zip(spice.items(), i)]
            s_foods = [sum(_) for _ in zip(*cur_foods)]
            if any(_ <= 0 for _ in s_foods):
                continue
            ms = 1
            for _ in s_foods:
                ms *= _
            max_sum = max(max_sum, ms)
    return max_sum

print(gsum(100, spicies))