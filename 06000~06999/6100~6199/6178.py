"""
[6178: Lake Making](https://www.acmicpc.net/problem/6178)

Tier: Bronze 1 
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
  R, C, E, N = mii()
  l = [mii() for _ in range(R)]
  queries = [mii() for _ in range(N)]

  for r, c, d in queries:
    mx = 0
    r -= 1
    c -= 1

    for i in range(r, r + 3):
      for j in range(c, c + 3):
        if i >= R or j >= C:
          continue
        mx = max(mx, l[i][j])
    
    for i in range(r, r + 3):
      for j in range(c, c + 3):
        if i >= R or j >= C:
          continue
        l[i][j] = min(l[i][j], mx - d)
  
  ans = 0

  for i in l:
    for j in i:
      ans += max(0, E - j)

  p(ans * 72 * 72)  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
