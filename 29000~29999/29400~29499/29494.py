"""
[29494: Простая задача](https://www.acmicpc.net/problem/29494)

Tier: Bronze 1 
Category: ad_hoc, bruteforcing
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
  l = [mii() for _ in range(3)]

  for center in range(3):
    for k1 in range(4):
      for k2 in range(4):
        if k1 == k2:
          continue

        a = (center + 1) % 3
        b = (center + 2) % 3

        if l[center][k1] in l[a] and l[center][k2] in l[b]:
          return True
  
  return False


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    print("Yes" if ret else "No")
