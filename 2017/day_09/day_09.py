import re


data = open('data.txt').read().strip('\n')
#print(data)


def escape(data):
    accumulate = []
    trash = False
    skip = 0
    garbage = 0
    for i in range(len(data)):
        if skip:
            skip -= 1
            continue

        l = data[i]
        if l == '!':
            skip = 1
            continue
        if l == '<':
            if trash:
                garbage += 1
            trash = True
            continue
        if l == '>':
            trash = False
            continue
        if trash:
            garbage += 1
            continue
        accumulate.append(data[i])
    print('garbage is %s' % garbage)
    return ''.join(accumulate)

def group_score(row):
    score = 0
    g = 0
    for r in row:
        if r == '{':
            g += 1
            score += g
        elif r == '}':
            g -= 1
    return score


print(group_score(escape(data)))
print(group_score(escape('<{o"i!a,<{i<a>')))