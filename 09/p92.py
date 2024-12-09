#!/usr/bin/env python3


file = open('input.txt', 'r')
m = file.readline()
l = len(m.rstrip())

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

l = len(output)

jump = 0
for i in reversed(range(len(output))):
    if jump > 0:
        jump = jump - 1
        continue
    if output[i] == '.':
        continue
    t = i
    while t > 0 and output[t-1] == output[i]:
        t = t - 1
    n = i - t + 1
    for j in range(len(output)):
        if j > i: break
        if output[j] == '.':
            space = True
            # Check contiguous:
            if j+n <= l:
                for jj in range(n):
                    if output[j+jj] != ".":
                        space = False
                        break
                if space:
                    # insert it
                    for jj in range(n):
                        output[j+jj] = output[i-jj]
                        output[i-jj] = '.'
                    #print(output)
                    break
                else:
                    continue
    jump = n -1
#print(output)

res = 0
for i in range(len(output)):
    if output[i] != '.':
        res = res + i * int(output[i])
print(res)
