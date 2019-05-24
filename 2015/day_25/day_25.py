def srange(a, b):
    n = b - a
    return int((b-a+1) * (b+a) / 2)

def coordinator():
    shift = 1
    r, c = 1, 0
    n = 2
    while True:
        yield (n, r+1, c+1)
        n += 1
        if r-1 < 0:
            r += shift + 1
            c -= shift
            shift += 1
        else:
            r -= 1
            c += 1

'''To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075.'''

R = 2981
C = 3075

P = 252533
Q = 33554393
key = 20151125

i = 0
for n, r, c in coordinator():
    i += 1
    key = (key*P) % Q
    if r == R and c == C:
        print(n, r, c, key, i)
        break