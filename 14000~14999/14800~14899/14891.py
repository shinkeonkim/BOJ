"""
[14891: 톱니바퀴](https://www.acmicpc.net/problem/14891)

Tier: Gold 5 
Category: implementation, simulation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from functools import reduce, lru_cache
from operator import itemgetter, attrgetter, mul, add, sub, truediv
from typing import List, Tuple, Dict, Set, Any, Union
from fractions import Fraction

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]

def rotate_clockwise(gear):
  return [gear[-1]] + gear[:-1]

def rotate_counterclockwise(gear):
  return gear[1:] + [gear[0]]


def solve():
  gears = [['']]+[list(input()) for _ in range(4)]
  
  k = ii()
  
  for _ in range(k):
    num, rotate = mii()
    rotate_info = [0] * 5
    
    rotate_info[num] = rotate
    
    for i in range(num, 4):
      if gears[i][2] != gears[i+1][6]:
        rotate_info[i+1] = -rotate_info[i]
      else:
        rotate_info[i+1] = 0
        break
    
    for i in range(num, 1, -1):
      if gears[i-1][2] != gears[i][6]:
        rotate_info[i-1] = -rotate_info[i]
      else:
        rotate_info[i-1] = 0
        break       
    
    # print(rotate_info)
  
    for i in range(1, 5):
      if rotate_info[i] == 1:
        gears[i] = rotate_clockwise(gears[i])
      elif rotate_info[i] == -1:
        gears[i] = rotate_counterclockwise(gears[i])

  ans = 0
  for i in range(1, 5):
    if gears[i][0] == '1':
      ans += 2**(i-1)
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
