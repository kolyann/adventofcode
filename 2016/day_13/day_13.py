from random import randint
import sys

inp = 1364


def wall(x, y, inp=inp):
    v = x*x + 3*x + 2*x*y + y + y*y + inp
    return sum(map(int, bin(v)[2:])) % 2

moves = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

def walk_around(fx, fy, num=inp, part2=0):
    paths = [(1, 1, 0)]
    walls = set()
    visited = set()

    visited_p2 = set()

    while paths:
        n_paths = set()
        for x, y, step in paths:
            visited.add((x, y))
            if part2:
                visited_p2.add((x, y))
            if x == fx and y == fy and not part2:
                return step
            for xm, ym in moves:
                _x, _y = x+xm, y+ym
                if _x < 0 or _y < 0:
                    continue
                if (_x, _y) in walls or (_x, _y) in visited:
                    continue

                if wall(_x, _y, num):
                    walls.add((_x, _y))
                else:
                    if not part2 or (part2 and step < part2):
                        n_paths.add((_x, _y, step+1))
        paths = n_paths

    if part2:
        def ddraw():
            cx = 0
            coords = walls.union(visited)
            max_x = max(coords, key=lambda f: f[0])[0]
            max_y = max(coords, key=lambda f: f[1])[1]
            draw = [[' ' for j in range(max_y+1)] for i in range(max_x+1)]
            for x, y in coords:
                draw[x][y] = '#' if wall(x, y, num) else '.'
            for r in draw:
                for c in r:
                    print(c, end='')
                print()

        return len(visited_p2), ddraw


print(walk_around(31, 39, num=inp))
print(walk_around(31, 39, num=inp, part2=50))


# for j in range(0, 100000):
#     i = randint(0, sys.maxsize)
#     n, f = walk_around(0, 0, i, 10000)
#     if n > 1000:
#         f()
#         print(i, n)
#         print('\n'*5)