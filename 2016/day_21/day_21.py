from itertools import permutations

def try_to_int(x):
    try:
        return int(x)
    except:
        return x

def parse(s, commands):
    s = list(s)
    #print(s)
    for cmd in commands:
        cmd = list(map(try_to_int, cmd.strip().split(' ')))
        if cmd[0] == 'move':
            c = s.pop(cmd[2])
            s.insert(cmd[5], c)
        elif cmd[0:2] == ['swap', 'letter']:
            s = list(''.join(s).replace(cmd[2], '*').replace(cmd[5], cmd[2]).replace('*', cmd[5]))
        elif cmd[0:2] == ['swap', 'position']:
            s[cmd[2]], s[cmd[5]] = s[cmd[5]], s[cmd[2]]
        elif cmd[0] == 'rotate':
            if cmd[1] == 'left':
                s = s[cmd[2]:] + s[:cmd[2]]
            elif cmd[1] == 'right':
                s = s[-cmd[2]:] + s[:-cmd[2]]
            elif cmd[1] == 'based':
                ind = s.index(cmd[-1])
                if ind >= 4:
                    ind += 1
                ind += 1
                ind %= len(s)
                s = s[-ind:] + s[:-ind]
        elif cmd[0] == 'reverse':
           s[cmd[2]:cmd[4]+1] = reversed(s[cmd[2]:cmd[4]+1])
        else:
            raise Exception("Unexcepted command %s" % cmd)

        #print('{}\t{}'.format(s, cmd))
    return ''.join(s)

def unscramble(s, commands):
    for perm in permutations(s):
        if parse(perm, commands) == s:
            return ''.join(perm)

cmds = open('data.txt').readlines()

print(parse('abcdefgh', cmds))
print(unscramble('fbgdceah', cmds))

