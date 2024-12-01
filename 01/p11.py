#!/usr/bin/env python

"Solution for exercise 1.1"

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

print(sum(list(map(abs, list(map(sub, sorted(list2), sorted(list1)))))))
