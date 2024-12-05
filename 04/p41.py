#!/usr/bin/env python3

file = open('input.txt', 'r')
#lines = list(map(to_report, sys.stdin.readlines()))
m = file.readlines()
h = len(m)
l = len(m[0].rstrip())
total = 0

m2 = [[ '.' for i in range(l)] for j in range(h)]

for x in range(h):
    for y in range(l):
        #h ->
        if y < l-3:
            if m[x][y] == 'X' and m[x][y+1] == 'M' and m[x][y+2] == 'A' and m[x][y+3] == 'S':
                m2[x][y]='X'; m2[x][y+1]='M'; m2[x][y+2]='A'; m2[x][y+3] = 'S'
                total = total + 1
        #h <b-
        if y >= 3:
            if m[x][y] == 'X' and m[x][y-1] == 'M' and m[x][y-2] == 'A' and m[x][y-3] == 'S':
                m2[x][y]='X'; m2[x][y-1]='M'; m2[x][y-2]='A'; m2[x][y-3] = 'S'
                total = total + 1

        #v down
        if x < h-3:
            if m[x][y] == 'X' and m[x+1][y] == 'M' and m[x+2][y] == 'A' and m[x+3][y] == 'S':
                m2[x][y]='X'; m2[x+1][y]='M'; m2[x+2][y]='A'; m2[x+3][y] = 'S'
                total = total + 1
        #v up
        if x >= 3:
            if m[x][y] == 'X' and m[x-1][y] == 'M' and m[x-2][y] == 'A' and m[x-3][y] == 'S':
                m2[x][y]='X'; m2[x-1][y]='M'; m2[x-2][y]='A'; m2[x-3][y] = 'S'
                total = total + 1
        
        #diagonal right up
        if x >= 3 and y < l-3:
            if m[x][y] == 'X' and m[x-1][y+1] == 'M' and m[x-2][y+2] == 'A' and m[x-3][y+3] == 'S':
                m2[x][y]='X'; m2[x-1][y+1]='M'; m2[x-2][y+2]='A'; m2[x-3][y+3] = 'S'
                total = total + 1

        #diagonal right down
        if x < h-3 and y < l-3:
            if m[x][y] == 'X' and m[x+1][y+1] == 'M' and m[x+2][y+2] == 'A' and m[x+3][y+3] == 'S':
                m2[x][y]='X'; m2[x+1][y+1]='M'; m2[x+1][y+2]='A'; m2[x+3][y+3] = 'S'
                total = total + 1

        #diagonal left up
        if x >= 3 and y >= 3:
            if m[x][y] == 'X' and m[x-1][y-1] == 'M' and m[x-2][y-2] == 'A' and m[x-3][y-3] == 'S':
                m2[x][y]='X'; m2[x-1][y-1]='M'; m2[x-2][y-2]='A'; m2[x-3][y-3] = 'S'
                total = total + 1

        #diagonal left down
        if x < h-3 and y >= 3:
            if m[x][y] == 'X' and m[x+1][y-1] == 'M' and m[x+2][y-2] == 'A' and m[x+3][y-3] == 'S':
                m2[x][y]='X'; m2[x+1][y-1]='M'; m2[x+2][y-2]='A'; m2[x+3][y-3] = 'S'
                total = total + 1

for x in range(h):
    print(m2[x])

print(total)