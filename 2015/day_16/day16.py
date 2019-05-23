code = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''
code = {x[0].split(':')[0]: int(x[0].split(':')[1].strip()) for x in [k.split('\n') for k in code.split('\n')]}

sues = [{ks: dict([(k[0], int(k[1].strip())) for k in map(lambda x: x.strip().split(':'), f.split(','))])} for ks, f in {x[0]:x[1] for x in [s.strip().split(':', 1) for s in open('data.txt')]}.items()]


def equal(k, v, code):
    if k in ('cats', 'trees'):
        return v > code[k]
    elif k in ('pomeranians', 'goldfish'):
        return v < code[k]
    else:
        return v == code[k]


for sue in sues:
    item = list(sue.values())[0].items()
    if all(equal(x, y, code) for x, y in item):
        print('Part2 %s' % sue)
    if all(code[x] == y for x, y in item):
        print('Part1 %s' % sue)
