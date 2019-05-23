import re
import string
from html import escape
data = open("data.txt")

data = list(map(str.strip, data))
part = 2

chrs = 0
symbols = 0
for line in data:
    if part == 1:
        chrs += len(line)

        nline = re.sub(r'(^\"|\"$)', '', line)
        nline = re.sub(r'\\\"', '"', nline)
        nline = nline.replace("\\\\", ",")
        nline = re.sub(r'\\x\w\w', '.', nline)

        symbols += len(nline)
        if len(nline) != len(eval(line)):
            print('{:3d} {:3d} {:3d} {:s} {:s}'.format(len(line), len(nline), len(eval(line)), line, nline))
    else:
        chrs += len(line)
        nline = re.sub(r'\\\\', r',,,,', line)
        nline = re.sub(r'(\\x(\w\w))', r'\\\\x\2', nline)
        nline = re.sub(r'\\\"', '\\\\\\"', nline)
        nline = re.sub(r'\"', '\\\\"', nline)

        symbols += (len(nline) + 2)
        print('{:3d} {:3d} {:13s} {:s}'.format(len(line), 2+len(nline), line, nline))

print(chrs, symbols, symbols-chrs)