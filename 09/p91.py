#!/usr/bin/env python3

print("hello")

file = open('input.txt', 'r')
m = file.readline()
l = len(m.rstrip())
print(l)

file = True
file_id = 0
output = []
for i in range(l):
    x = m[i]
    if file:
        for j in range(int(x)):
            output.append(str(file_id))
        file = False
        file_id = file_id + 1
    else:
        for j in range(int(x)):
            output.append(".")
        file = True

for i in range(len(output)):
    if output[i] == ".":
        for j in reversed(range(len(output))):
            if output[j] != '.' and j > i:
                output[i] = output[j]
                output[j] = '.'
                break
res = 0
for i in range(len(output)):
    if output[i] != '.':
        res = res + i * int(output[i])
print(res)

