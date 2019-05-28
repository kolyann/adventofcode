import re
from pprint import pprint
ss = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''

def parse_progs(inp):
    data = {}
    for i in inp:
        n, nums = re.split(r' \<\-\> ', i)
        data[int(n)] = set(int(s.strip()) for s in nums.split(','))
    return data

def grouppirize(inp_data):
    data = dict(inp_data)
    changed = True
    while changed:
        changed = False
        for k, v in data.items():
            for n in [_ for _ in v]:
                for s in [_ for _ in data[n]]:
                    if k not in data[s]:
                        data[s].add(k)
                        changed = True
    return len(data[0]), data.values()


ans = grouppirize(parse_progs(open('data.txt')))
print(len(set(map(lambda x: tuple(sorted(tuple(x))), ans[1]))))