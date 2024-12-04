import re

def multiply(line):
    m = 0
    for x in re.finditer( r'mul\((\d{1,3}),(\d{1,3})\)', line):
        m += int(x.group(1)) * int(x.group(2))
    return m

with open('input.txt', 'r') as file:
    res = 0
    for line in file:
        res += multiply(line)
    print(res)
