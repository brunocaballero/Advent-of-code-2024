#!/usr/bin/env python3

from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

def next_direction(direction):    
    match direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP

def out(x,y):
    if x == -1 or y == -1 or x == h or y == l:
        return True
    else:
        return False

def next_position(x, y, direction):
    match direction:
        case Direction.UP:
            return x-1, y
        case Direction.RIGHT:
            return x, y+1
        case Direction.DOWN:
            return x+1, y
        case Direction.LEFT:
            return x, y-1

def run_maze_to_exit(lab):
    p_x = init_x
    p_y = init_y
    counter = 0
    direction = Direction.UP
    ## Do the 
    while True:
        counter = counter + 1
        if counter > h * l:
            return False
        n_x,n_y = next_position(p_x,p_y, direction)
        if out(n_x,n_y):
            return True
        if lab[n_x][n_y] == '#':
            direction = next_direction(direction)
            continue
        else:
            p_x = n_x
            p_y = n_y




file = open('input.txt', 'r')
#lines = list(map(to_report, sys.stdin.readlines()))
m = file.readlines()
h = len(m)
l = len(m[0].rstrip())

m2 = [[ '.' for i in range(l)] for j in range(h)]

init_x = 0
init_y = 0
direction = Direction.UP

# find first position
for x in range(h):
    for y in range(l):
        if m[x][y] == '^':
            init_x = x
            init_y = y
            break

loops = 0
for x in range(h):
    for y in range(l):
        lab = m
        if m[x][y] == '.':
            lab[x] = list(m[x])
            lab[x][y] = '#'
            print("{} {}",x,y)
            if not run_maze_to_exit(lab):
                loops = loops +1
            lab[x][y] = '.'

print(loops)
