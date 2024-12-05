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

def correct_order(numbers):
    changed = True
    while changed:
        changed = False
        for i in range(len(numbers)):
            for r in rules:
                if numbers[i] == r[1] and r[0] in numbers[i:]:
                    index = numbers.index(r[0])
                    numbers[i] = r[0]
                    numbers[index] = r[1]
                    changed = True
    return numbers

sum = 0

file = open('input.txt', 'r')
for line in file:
    r = re.search(r'(\d+)\|(\d+)', line)
    if r:
        add_rules(int(r.group(1)), int(r.group(2)))
    
    if re.match(r'\d+,\d+.*', line):
        numbers = list(map(int, line.split(',')))
        if not check_order(numbers):
            ordered_numbers = correct_order(numbers)
            m = len(ordered_numbers)//2
            sum = sum + ordered_numbers[m]

print(sum)
