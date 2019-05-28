from math import ceil

direct = {'nw': (-1, -1), 'n': (-2, 0), 'ne': (-1, 1), 'sw': (1, -1), 's': (2, 0), 'se': (1, 1)}


def dist(x, y):
    return ceil((abs(x)+abs(y))/2)


def walk(path, p2=False):
    x = y = 0
    max_path = 0
    for p in path:
        x_, y_ = direct[p]
        x += x_
        y += y_
        max_path = max(max_path, dist(x, y))
    if not p2:
        return dist(x, y)
    else:
        return max_path


path = open('data.txt').readlines()[0].split(',')
print(walk(path))
print(walk(path, p2=True))