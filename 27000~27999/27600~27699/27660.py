"""
[27660: Queue skipping (Hard)](https://www.acmicpc.net/problem/27660)

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
  input()

  n, e = mii()
  l = [ii() for _ in range(e)]

  d = {}

  for i in range(1, n + 1):
    d[i] = i

  k = 0

  for i in l:
    d[i] = k
    k -= 1

  return sorted(d.items(), key = lambda t : (-t[1]))[0][0]

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

    p(ret)
