#!/usr/bin/env python3
import re

rules = []

def add_rules(a, b):
    rules.append([a, b])

def check_order(numbers):
    for i in range(len(numbers)):
        for r in rules:
            if numbers[i] == r[1] and r[0] in numbers[i:]:
                return False
    return True

sum = 0

file = open('input.txt', 'r')
for line in file:
    r = re.search(r'(\d+)\|(\d+)', line)
    if r:
        add_rules(int(r.group(1)), int(r.group(2)))
    
    if re.match(r'\d+,\d+.*', line):
        numbers = list(map(int, line.split(',')))
        if check_order(numbers):
            m = len(numbers)//2
            sum = sum + numbers[m]

print(sum)
