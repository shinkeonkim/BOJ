"""
[5077: Maps](https://www.acmicpc.net/problem/5077)

Tier: Bronze 1 
Category: bruteforcing, implementation, string
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
  target = [inp() for _ in range(n)]

  y, x = mii()
  mp = [inp() for _ in range(y)]

  count = 0
  for i in range(y - n + 1):
    for j in range(x - m + 1):
      found = True
      for k in range(n):
        for l in range(m):
          if target[k][l] != mp[i + k][j + l]:
            found = False
            break
        if not found:
          break
      if found:
        count += 1

  print(count)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
