"""
[26554: Draw](https://www.acmicpc.net/problem/26554)

Tier: Bronze 1 
Category: implementation
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

# 3
# rectangle 3 5 n
# right triangle 4 n
# diamond 7 y

def solve():
  query = input().split()
  grid = []
  
  if query[0] == "rectangle":
    a, b = int(query[1]), int(query[2])
    filled = query[3] == 'y'
    grid = [[' '] * (b + 2) for _ in range(a + 2)]

    for i in range(1, a + 1):
      for j in range(1, b + 1):
        grid[i][j] = '#'

  elif query[0] == 'left':
    a = int(query[2])
    filled = query[3] == 'y'
    grid = [[' '] * (a + 2) for _ in range(a + 2)]

    for i in range(1, a + 1):
      for j in range(1, i + 1):
        grid[i][j] = '#'

  elif query[0] == 'right':
    a = int(query[2])
    filled = query[3] == 'y'
    grid = [[' '] * (a + 2) for _ in range(a + 2)]

    for i in range(1, a + 1):
      for j in range(1, i + 1):
        grid[i][a + 1 - j] = '#'

  elif query[0] == 'diamond':
    a = int(query[1])
    filled = query[2] == 'y'
    
    grid = [[' '] * (a + 2) for _ in range(a + 2)]

    for i in range(1, a + 1):
      for j in range(1, a + 1):
        if abs(i - (a // 2 + 1)) + abs(j - (a // 2 + 1)) <= a // 2:
          grid[i][j] = '#'
        else:
          grid[i][j] = ' '

  for i in range(1, len(grid) - 1):
    ret = ""
    for j in range(1, len(grid[i]) - 1):
      if not filled:
        cnt = 0
        
        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0)]:
          if grid[i + dy][j + dx] == ' ':
            cnt += 1
        if grid[i][j] == '#' and cnt > 0:
          ret += grid[i][j]
        else:
          ret += ' '
      else:
        ret += grid[i][j]

    print(ret.rstrip())


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
