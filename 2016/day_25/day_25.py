# Fork day 12

class Register:

    def __init__(self, a=0):

        self.values = {i: 0 for i in 'abcd'}
        self.values['a'] = a


    def eval(self, expression):
        exp = expression.strip().split(' ')
        cmd = exp[0]
        if cmd == 'cpy':
            try:
                self.values[exp[2]] = self.values[exp[1]]
                return True, 1
            except KeyError:
                self.values[exp[2]] = int(exp[1])
                return True, 1
        elif cmd == 'inc':
            self.values[exp[1]] += 1
            return True, 1
        elif cmd == 'dec':
            self.values[exp[1]] -= 1
            return True, 1
        elif cmd == 'jnz':
            try:
                if self.values[exp[1]]:
                    return True, int(exp[2])
                else:
                    return True, 1
            except KeyError:
                if int(exp[1]):
                    return True, int(exp[2])
                else:
                    return True, 1
        elif cmd == 'out':
            return False, self.values[exp[1]]
        else:
            raise Exception("Command not found: %s" % cmd)

    def __repr__(self):
        return str(self.values)


def odder(l, k=0):
    for i, s in enumerate(l):
        if s % 2 != (i + k) % 2:
            return False
    return True

def evaluate_commands(cmds, l=20, a=0):
    reg = Register(a=a)
    i = 0
    signal = []
    while True:
        #print(reg, cmds[i])
        try:
            #print('Run {:3d}   {:9s}'.format(i, cmds[i]).strip('\n\r'))
            (r, n) = reg.eval(cmds[i])
            if r:
                i += n
            if not r:
                i += 1
                signal.append(n)
                if not (odder(signal) or odder(signal, 1)):
                    return False
                elif len(signal) >= l:
                    return signal
        except IndexError as e:
            return signal




dt = open('data.txt').readlines()

for t in range(10**10):
    res = evaluate_commands(dt, l=10, a=t)
    if res:
        print(t, res)
        #break
