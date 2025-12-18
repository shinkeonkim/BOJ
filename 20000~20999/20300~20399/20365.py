"""
[20365: 블로그2](https://www.acmicpc.net/problem/20365)

Tier: Silver 3 
Category: greedy, string
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
  s = inp()

  b_area = 0
  r_area = 0

  crt = s[0]
  
  for i in range(1, n):
    if s[i] != crt:
      if crt == "B":
        b_area += 1
      else:
        r_area += 1
      crt = s[i]
  
  if crt == "B":
    b_area += 1
  else:
    r_area += 1
  
  p(min(b_area, r_area) + 1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
