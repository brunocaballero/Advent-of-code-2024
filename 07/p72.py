#!/usr/bin/env python3


def bitfield(n,l):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:].zfill(l)]

def ternary(n, l):
    #if n == 0:
    #    return '0'.zfill(l)
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.insert(0,r)
    while len(nums) < l:
        nums.insert(0,0)
    return nums

def operate(numbers, operands):
    res = numbers[0]
    for i in range(len(operands)):
        if operands[i] == 0:
            res = res + numbers[i+1]
        elif operands[i] == 1:
            res = res * numbers[i+1]
        else:
            ## TODO: Concatenate
            res = int(str(res) + str(numbers[i+1]))
    return res 

def check(res, numbers):
    l = len(numbers)-1
    n_operands = 3**l
    for x in range(n_operands):
        operands = ternary(x,l)
        if operate(numbers, operands) == res:
            return True
    return False



counter = 0
with open('input.txt', 'r') as file:
    for line in file:
        groups = line.split(":")
        res = int(groups[0])
        numbers = list(map(int, groups[1].strip().rstrip().split(" ")))
        if check(res, numbers):
            counter = counter + res 

print(counter)
