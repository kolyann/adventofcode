from itertools import combinations, permutations
import sys

f = map(int, map(str.strip, open('data.txt')))
nums = list(enumerate(f))

fin = 150
cnt = 0

min_amnt = sys.maxsize

for i in range(2, len(nums)+1):
    for c in combinations(nums, i):
        c = [_[1] for _ in c]
        if sum(c) == fin:
            cnt += 1
            min_amnt = min(min_amnt, len(c))
            # print(c)

print('Part1 %s' % cnt)
print(min_amnt)

diff_min_cnt = 0
for i in range(2, len(nums)+1):
    for c in combinations(nums, i):
        c = [_[1] for _ in c]
        if sum(c) == fin and len(c) == min_amnt:
            diff_min_cnt += 1

print('Part2 %s' % diff_min_cnt)
