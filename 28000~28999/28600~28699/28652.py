"""
[28652: Японский кроссворд](https://www.acmicpc.net/problem/28652)

Tier: Bronze 1 
Category: implementation, string
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


def solve():
  n, m = mii()

  grid = [inp() for _ in range(n)]

  rows = []
  cols = []

  for i in range(n):
    current = []

    cnt = 0

    for j in range(m):
      if grid[i][j] == '#':
        cnt += 1
      else:
        if cnt > 0:
          current.append(cnt)
        cnt = 0
    if cnt > 0:
      current.append(cnt)
    rows.append(current)
  
  for j in range(m):
    current = []
    cnt = 0

    for i in range(n):
      if grid[i][j] == '#':
        cnt += 1
      else:
        if cnt > 0:
          current.append(cnt)
        cnt = 0
    if cnt > 0:
      current.append(cnt)
    cols.append(current)
  
  for i in range(n):
    print(len(rows[i]), *rows[i])
  
  print()

  for j in range(m):
    print(len(cols[j]), *cols[j])

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
