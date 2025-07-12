"""
[19842: Restoring the Sequence](https://www.acmicpc.net/problem/19842)

Tier: Bronze 1 
Category: implementation
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
  m = ii()
  a = mii()

  not_expected = []
  i = 1
  idx = 0
  while i <= n and idx < m:
    if i != a[idx]:
      not_expected.append(i)
      i += 1
      continue
    i += 1
    idx += 1
  
  while i <= n:
    not_expected.append(i)
    i += 1
  
  while idx < m:
    not_expected.append(a[idx])
    idx += 1

  if len(not_expected) == 1:
    print("Yes")
    print(not_expected[0])
  else:
    print("No")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
