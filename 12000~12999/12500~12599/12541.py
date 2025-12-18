"""
[12541: Building a House (Small)](https://www.acmicpc.net/problem/12541)

Tier: Silver 4 
Category: prefix_sum
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
def round_up_half(n): return floor(n + 0.5)


def solve():
  # W, R, T 는 제거 불가능

  m, n = mii()

  grid = [input() for _ in range(n)]
  ans = 0

  for i in range(n):
    for j in range(m):
      for y in range(n - i):
        for x in range(m - j):
          is_valid = True
      
          for yy in range(i, i + y + 1):
            for xx in range(j, j + x + 1):
              if grid[yy][xx] in "WRT":
                is_valid = False
                break
            if not is_valid:
              break
          if is_valid:
            ans = max(ans, (y + 1) * (x + 1))

  return ans


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret}")
