
class Register:

    def __init__(self, c=0):

        self.values = {i: 0 for i in 'abcd'}
        self.values['c'] = c


    def eval(self, expression):
        exp = expression.strip().split(' ')
        cmd = exp[0]
        if cmd == 'cpy':
            try:
                self.values[exp[2]] = self.values[exp[1]]
                return True, 0
            except KeyError:
                self.values[exp[2]] = int(exp[1])
                return True, 0
        elif cmd == 'inc':
            self.values[exp[1]] += 1
            return True, 0
        elif cmd == 'dec':
            self.values[exp[1]] -= 1
            return True, 0
        elif cmd == 'jnz':
            try:
                if self.values[exp[1]]:
                    return False, int(exp[2])
                else:
                    return True, 0
            except KeyError:
                if int(exp[1]):
                    return False, int(exp[2])
                else:
                    return True, 0

        else:
            raise Exception("Command not found: %s" % cmd)

    def __repr__(self):
        return str(self.values)


def evaluate_commands(cmds, c=0):
    reg = Register(c=c)
    i = 0
    while True:
        try:
            #print('Run {:3d}   {:9s}'.format(i, cmds[i]).strip('\n\r'))
            (r, n) = reg.eval(cmds[i])
            if r:
                i += 1
            if not r:
                i += n
        except IndexError as e:
            return reg.values['a']




t = evaluate_commands(open('data.txt').readlines())
print(t)

p2 = evaluate_commands(open('data.txt').readlines(), c=1)
print(p2)