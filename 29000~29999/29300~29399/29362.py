"""
[29362: Дом семьи Гарнетт](https://www.acmicpc.net/problem/29362)

Tier: Bronze 1 
Category: math, arithmetic
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
  l = [mii() for _ in range(n)]
  points = []

  for i in range(n):
    for j in range(m):
      if l[i][j] == 1:
        points.append((i, j))
  
  ans = 0

  if points[0][0] != points[1][0]:
    mx = max(points[0][0], points[1][0])
    mn = min(points[0][0], points[1][0])

    k = (mn + 1) * m
    ans = max(ans, k)
    ans = max(ans, n * m - k)

    k = mx * m
    ans = max(ans, k)
    ans = max(ans, n * m - k)
  
  if points[0][1] != points[1][1]:
    mx = max(points[0][1], points[1][1])
    mn = min(points[0][1], points[1][1])

    k = (mn + 1) * n
    ans = max(ans, k)
    ans = max(ans, n * m - k)

    k = mx * n
    ans = max(ans, k)
    ans = max(ans, n * m - k)

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
