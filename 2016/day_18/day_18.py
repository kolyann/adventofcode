trap_set = {(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)}

def rtn(r):
    return tuple(0 if s=='.' else 1 for s in r)


def row_generator(init_row):
    trap_set = {(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)}
    row = rtn(init_row)
    yield(row)
    while True:
        row = (0, *row, 0)
        row = tuple(int(row[i-1:i+2] in trap_set) for i in range(1, len(row)-1))
        yield row

def calc_field(st_row, length):
    i = 0
    safe = 0
    rower = row_generator(st_row)
    for _, row in zip(range(length), rower):
        safe += len(row) - sum(row)
    return safe


init_row = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'

print(calc_field(init_row, 40))
print(calc_field(init_row, 400000))
