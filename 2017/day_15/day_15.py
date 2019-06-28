'''Generator A starts with 634
Generator B starts with 301'''

A = 634
B = 301


def gen(init, factor, part2=1):
    v = init
    m = 2**16
    while True:
        v = (v * factor) % 2147483647
        if v % part2 == 0:
            yield bin(v % m)


def count_pairs(n, init_a, init_b, p2_a=1, p2_b=1):
    s = 0
    a = gen(init_a, 16807, p2_a)
    b = gen(init_b, 48271, p2_b)
    for x, y, _ in zip(a, b, range(n)):
        s += (x==y)
    return s


print(count_pairs(40 * 10**6, A, B))
print(count_pairs(5 * 10**6, A, B, 4, 8))

