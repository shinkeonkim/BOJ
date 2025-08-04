"""
[12404: Recycled Numbers (Large)](https://www.acmicpc.net/problem/12404)

Tier: Silver 1 
Category: bruteforcing
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

group = {}

def smallest_number(n):
  ns = str(n)
  ret = n

  for i in range(1, len(ns)):
    new_ns = ns[i:] + ns[:i]

    if new_ns[0] == '0':
      continue

    ret = min(ret, int(new_ns))
  
  return ret


def solve():
  a, b = mii()

  d = defaultdict(lambda: 0)
  ans = 0

  for i in range(a, b + 1):
    d[group[i]] += 1
  
  for k, v in d.items():
    if v >= 2:
      ans += (v * (v - 1)) // 2

  return ans


if __name__ == "__main__":
  tc = ii()
  
  for i in range(1, 2000001):
    group[i] = smallest_number(i)

  for t in range(1, tc+1):
    ret = solve()

    print(f"Case #{t}: {ret}")
