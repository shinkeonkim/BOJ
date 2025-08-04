"""
[24176: 出前配達](https://www.acmicpc.net/problem/24176)

Tier: Silver 5 
Category: math, arithmetic, physics
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


def solve(n, m):
  l = [[*map(int, list(input()))] for _ in range(n)]

  d = [0, 0]
  s = [0, 0]

  for i in range(n):
    for j in range(m):
      d[0] += l[i][j] * (i + 1)
      d[1] += l[i][j] * (j + 1)
      s[0] += l[i][j]
      s[1] += l[i][j]

  print(d[0] / s[0], d[1] / s[1])


if __name__ == "__main__":
  while 1:
    n, m = map(int, input().split())
    if n == m == 0:
      break

    solve(n, m)