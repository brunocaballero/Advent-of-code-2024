#!/usr/bin/env python3

def mark_antinode(x,y):
    if x >= 0 and y >= 0 and x < h and y < l:
        m2[x][y] = '#'

def calculate_antinodes(x,y,x2,y2):

    dist_x = abs(x2 - x)
    dist_y = abs(y2 - y)
    if dist_x == 0 and dist_y == 0:
        return
    
    limit = max(h,l)
    for p in range(limit):
        mark_antinode((p+1)*x2 - p*x, (p+1)*y2 - p*y)
        mark_antinode((p+1)*x - p*x2, (p+1)*y - p*y2)
    
file = open('input.txt', 'r')
m = file.readlines()
h = len(m)
l = len(m[0].rstrip())

m2 = [[ '.' for i in range(l)] for j in range(h)]

for x in range(h):
    for y in range(l):
        if m[x][y] != '.':
            frequency = m[x][y]
            for x2 in range(h):
                for y2 in range(l):
                    if m[x2][y2] == frequency:
                        calculate_antinodes(x,y,x2,y2)

count = 0
for x in range(h):
    print(m2[x])
    for y in range(l):
        if m2[x][y] == '#':
            count = count + 1
print(count)
