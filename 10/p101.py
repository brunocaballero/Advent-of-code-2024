#!/usr/bin/env python3

# direction 0/UP 1/right 2/down 3/left, -1 

def next_slot(x,y,direction):
    match direction:
        case 0: #up
            x = x - 1
        case 1:
            y = y + 1
        case 2:
            x = x + 1
        case 3:
            y = y - 1
    if x < 0 or y < 0 or x >= h or y >= l:
        return (-1, -1)
    else:
        return (x, y)


def dfs(x, y):
    t = int(m[x][y])
    if t == 9:
        m2[x][y] = 1
        return
    for i in range(4):
        (x1, y1) = next_slot(x, y, i)
        if (x1, y1) != (-1,-1):
            if m[x1][y1] == str(t+1):
                dfs(x1,y1)

def dfsroot(x, y):
    count = 0
    for i in range(h):
        for j in range(l):
            m2[i][j] = 0
    dfs(x,y)
    for i in range(h):
        for j in range(l):
            if m2[i][j] == 1:
                count = count + 1
    return count

    #for i in range(h):
    #    print(m2[i])

file = open('input.txt', 'r')
m = file.readlines()
h = len(m)
l = len(m[0].rstrip())
m2 = [[0 for x in range(l)] for y in range(h)] 

all = 0
for x in range(h):
    for y in range(l):
        if m[x][y] == '0':
            all = all + dfsroot(x,y)

print(all)