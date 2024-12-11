#!/usr/bin/env python3

from functools import cache

@cache
def blink(x):
  if x == 0:
    return (1,)
  elif len(str(x)) % 2 == 0:
    d = len(str(x)) // 2
    left = str(x)[:d]
    right = str(x)[d:]
    return (int(left), int(right))
  else:
    return (x * 2024,)
  
@cache
def blink_repeat(x, n):
  xblinked = blink(x)
  if n == 1:
    return len(xblinked)
  return sum(map(lambda x: blink_repeat(x, n-1), xblinked))

with open("input.txt") as file:
  line = file.readline()
  stones = list(map(int, line.split()))
  print(sum(map(lambda x: blink_repeat(x,25), stones)))
  print(sum(map(lambda x: blink_repeat(x,75), stones)))
