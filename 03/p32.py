import re

def multiply(line):
    m = 0
    for x in re.finditer( r'mul\((\d{1,3}),(\d{1,3})\)', line):
       m += int(x.group(1)) * int(x.group(2))
    return m

def filter(line):
    enabled = True
    out = ""
    for x in re.findall(r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)", line):
        if x == "do()":
            enabled = True
        elif x == "don't()":
            enabled = False
        else:
            if enabled:
                out += x
    return out                      

with open('input.txt', 'r') as file:
    res = 0
    input = file.read()
    res += multiply(filter(input))
    print(res)
