"""
[28756: Перерыв на обед](https://www.acmicpc.net/problem/28756)

Tier: Bronze 1 
Category: arithmetic, bruteforcing, geometry, implementation, math
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

def dis(x1: int, y1: int, x2: int, y2: int) -> float:
  return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve():
  l = mii()
  n = ii()
  ans = float('inf')

  for _ in range(n):
    x, y, d = mii()

    ans = min(ans, dis(l[0], l[1], x, y) + d + dis(l[2], l[3], x, y))
  
  print(f"{ans:.10f}")



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
