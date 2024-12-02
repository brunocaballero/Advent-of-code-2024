#!/usr/bin/env python

"Solution for exercise 1.1"

import sys;

count = 0

def check_direction(levels):
    if len(levels) < 2:
        return False
    if (levels[1] > levels[0]):
        ascending = True
    elif (levels[1] < levels[0]):
        ascending = False
    else:
        return False    
    for i in range(1,len(levels)):
        if ascending and levels[i] <= levels[i-1]:
            return False
        elif not(ascending) and levels[i] >= levels[i-1]:
            return False
    return True


def check_increase(levels):  
    for i in range(1,len(levels)):
        diff = abs(levels[i]-levels[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

with open('input2.txt', 'r') as file:
    for line in file:
        levels = []
        groups = line.split()
        for i in range(0,len(groups)):
            levels.append(int(groups[i]))

        if check_direction(levels) and check_increase(levels):
            count = count +1

print(count)
        
                