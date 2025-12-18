"""
[10275: 골드 러시](https://www.acmicpc.net/problem/10275)

Tier: Bronze 1 
Category: math, implementation
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


def f(n: int, a: int, b: int) -> None:
  k = n // 2

  if n == a or n == b:
    return 0
  
  if n == 1:
    return 1

  if a < b:
    a, b = b, a
  
  assert(a >= k)

  # print(f"f({n}, {a}, {b})")

  return 1 + f(n - k, a - k, b)

def solve():
  n, a, b = mii()

  n = 2 ** n

  ret = f(n, a, b)

  print(ret)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
