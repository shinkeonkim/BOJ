"""
[34544: 후문으로](https://www.acmicpc.net/problem/34544)

Tier: Bronze 2 
Category: math, implementation, arithmetic, simulation
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
from fractions import Fraction

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
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]

def diff(a, b):
  if b > a:
    if a <= 0 <= b:
      return b - a - 1
    return b - a
  elif a > b:
    if b <= 0 <= a:
      return b - a + 1
    return b - a
  return 0

def add(a, b):
  if b > 0:
    if a <= 0 <= a + b:
      return a + b + 1
    return a + b
  elif b < 0:
    if a + b <= 0 <= a:
      return a + b - 1
    return a + b
  return a


def solve():
  n = ii()
  cur = 1
  for _ in range(n):
    a, b = mii()
    cur = add(cur, diff(a, b))
  p(cur)
    
    


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
