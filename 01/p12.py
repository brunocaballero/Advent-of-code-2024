#!/usr/bin/env python

"Solution for exercise 1.2"

import sys;
from operator import sub;

list1 = []
list2 = []

with open('input1.txt', 'r') as file:
    for line in file:
        groups = line.split()
        if len(groups) != 2:
            print("Error in input " + groups)
            sys.exit(-1)
        else:
            list1.append(int(groups[0]))
            list2.append(int(groups[1]))

count = 0
for x in list1:
    count += x * list2.count(x)

print(count)