"""
[9844: Gecko](https://www.acmicpc.net/problem/9844)

Tier: Silver 3 
Category: dp
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
  h, w = mii()
  grid = [[*map(int, input().split())] for _ in range(h)]

  dp = [0] * w
  for i in range(h):
    new_dp = [0] * w

    for j in range(w):
      new_dp[j] = dp[j]

      if j > 0:
        new_dp[j] = max(new_dp[j], dp[j-1])
      if j + 1 < w:
        new_dp[j] = max(new_dp[j], dp[j+1])
      new_dp[j] += grid[i][j]

    dp = new_dp
  
  print(max(dp))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
