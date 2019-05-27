import hashlib
from collections import namedtuple

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()[:4]

def open_doors(s):
    #the doors up, down, left, and right
    doors = ((-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'))
    return [d for d, h in zip(doors, s) if h in 'bcdef']

def walk(passphrase, part1=True):
    path_nt = namedtuple('path', ('x', 'y', 'way'))
    mx = 3
    my = 3
    paths = [path_nt(0, 0, '')]
    right_paths = []
    while paths:
        new_paths = []
        for path in paths:
            x, y, key = path
            if x == mx and y == my:
                if part1:
                    return key
                else:
                    right_paths.append(key)
                    continue
            doors = open_doors(md5(passphrase + key))
            for d in doors:
                if 0 <= x + d[0] <= mx and 0 <= y + d[1] <= my:
                    new_paths.append([x+d[0], y+d[1], key+d[2]])
        paths = new_paths
    if part1:
        return None
    else:
        return len(sorted(right_paths, key=len)[-1])



print(walk('dmypynyp'))
print(walk('dmypynyp', part1=False))
