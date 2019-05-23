import math

inp = 34000000



def qfactorize(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def qfac(n, last=50):
   return [q for q in qfactorize(n) if n//q <= 50]

def factorize(n):
    res = []
    i = 1
    while True:
        i += 1
        if i > n//2:
            break
        if n % i == 0:
            res.append(i)
    res.extend([1, n])
    return [i for i in res if n//i <= 50]


#print(factorize(9000))
i = 0
maxs = 0
while True:
    i += 1
    csum = sum([x*11 for x in qfac(i)])
    if csum > inp:
        print(i, csum)
        break
    if i % 10000 == 0:
        print(i, csum, '-')