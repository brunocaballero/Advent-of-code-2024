#!/usr/bin/env python3

file = open('input.txt', 'r')
#lines = list(map(to_report, sys.stdin.readlines()))
m = file.readlines()
h = len(m)
l = len(m[0].rstrip())
total = 0

m2 = [[ '.' for i in range(l)] for j in range(h)]

for x in range(h-2):
    for y in range(l-2):
        if m[x][y] == 'M' and m[x][y+2] == 'M' and m[x+1][y+1] == 'A' and m[x+2][y] == 'S' and m[x+2][y+2] == 'S':
            m2[x][y]='M'; m2[x][y+2]='M'; m2[x+1][y+1] ='A'; m2[x+2][y]='S'; m2[x+2][y+2]='S'
            total = total + 1
        
        if m[x][y] == 'M' and m[x][y+2] == 'S' and m[x+1][y+1] == 'A' and m[x+2][y] == 'M' and m[x+2][y+2] == 'S':
            m2[x][y]='M'; m2[x][y+2]='S'; m2[x+1][y+1] ='A'; m2[x+2][y]='M'; m2[x+2][y+2]='S'
            total = total + 1

        if m[x][y] == 'S' and m[x][y+2] == 'M' and m[x+1][y+1] == 'A' and m[x+2][y] == 'S' and m[x+2][y+2] == 'M':
            m2[x][y]='S'; m2[x][y+2]='M'; m2[x+1][y+1] ='A'; m2[x+2][y]='S'; m2[x+2][y+2]='M'
            total = total + 1

        if m[x][y] == 'S' and m[x][y+2] == 'S' and m[x+1][y+1] == 'A' and m[x+2][y] == 'M' and m[x+2][y+2] == 'M':
            m2[x][y]='S'; m2[x][y+2]='S'; m2[x+1][y+1] ='A'; m2[x+2][y]='M'; m2[x+2][y+2]='M'
            total = total + 1
        
for x in range(h):
    print(m2[x])

print(total)