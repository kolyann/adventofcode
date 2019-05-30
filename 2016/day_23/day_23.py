#day 12 fork

class Register:
    def __init__(self, start=None):
        self.values = {i: 0 for i in 'abcd'}
        self.values.update(start)

    def eval(self, expression):
        exp = self.parse(expression)
        cmd = exp[0]
        if cmd == 'cpy':
            try:
                self.values[exp[2]] = self.values[exp[1]]
                return False, 1
            except KeyError:
                self.values[exp[2]] = int(exp[1])
                return False, 1
        elif cmd == 'inc':
            self.values[exp[1]] += 1
            return False, 1
        elif cmd == 'dec':
            self.values[exp[1]] -= 1
            return False, 1
        elif cmd == 'jnz':
            jnz_exp = [exp[0]]
            for c in exp[1:]:
                try:
                    jnz_exp.append(self.values[c])
                except KeyError:
                    jnz_exp.append(int(c))
            if jnz_exp[1]:
                return False, jnz_exp[2]
            else:
                return False, 1

        elif cmd == 'tgl':
            return True, int(self.values[exp[1]])
        else:
            raise Exception("Command not found: %s" % cmd)

    @staticmethod
    def parse(expression):
        exp = expression.strip().split(' ')
        cmd = []
        for e in exp:
            try:
                cmd.append(int(e))
            except:
                cmd.append(e)
        return cmd


    def __repr__(self):
        return str(self.values)


def repl(cmd, tgl):
    cmd = Register.parse(cmd)
    cmd[0] = tgl
    return ' '.join(map(str, cmd)).strip()

def evaluate_commands(cmds, start=None):
    reg = Register(start)
    i = 0
    p = 0
    length = len(cmds)
    while True:
        if i==4: # Фрагмент оптимизации нагло подсмотренный на реддите
            reg.values['a'] = reg.values['b'] * reg.values['d']
            reg.values['c'] = 0
            reg.values['d'] = 0
            i = 10
            continue
        p+=1
        if i >= len(cmds):
            return reg

        (r, n) = reg.eval(cmds[i])
        if not r:
            i += n
        else: # tgl case
            k = i+n
            if k >= length:
                i += 1
                continue
            tgl = reg.parse(cmds[k])
            if len(tgl) == 2:
                if tgl[0] == 'inc':
                    cmds[k] = repl(cmds[k], 'dec')
                else:
                    cmds[k] = repl(cmds[k], 'inc')
            elif len(tgl) == 3:
                if tgl[0] == 'jnz':
                    cmds[k] = repl(cmds[k], 'cpy')
                else:
                    cmds[k] = repl(cmds[k], 'jnz')
            i += 1


commands = list(map(lambda x: x.strip(), open('data.txt').readlines()))
t = evaluate_commands(commands, start={'a': 12})

print(t)
