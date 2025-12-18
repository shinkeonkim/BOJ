"""
[26947: Klockan](https://www.acmicpc.net/problem/26947)

Tier: Bronze 1 
Category: bruteforcing, math
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
  n = ii()
  
  H = 0
  M = 0
  
  for h in range(0, 12):
    H = h * 300
    M = 0
    for m in range(0, 60):
      if H < M:
        k = M - H
      else:
        k = 3600 - (H - M)
      
      if k == n:
        p(f"{h:02d}:{m:02d}")
        return
  
      M += 60
      H += 5


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
