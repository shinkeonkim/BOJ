"""
[4934: The Euclidian Clock](https://www.acmicpc.net/problem/4934)

Tier: Bronze 1 
Category: geometry, math
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

SYS_INPUT = False
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


def to_tm(h, m, s, ms):
  return (h * 3600 + m * 60 + s) * 100 + ms

def tm_to_angle(mili):
  total = 12 * 3600 * 100

  return (mili / total) * 360

def diff(a, b):
  if a > b:
    return 360 - (a - b)
  return b - a

def solve():
  start = tm_to_angle(to_tm(*mii()))
  end = tm_to_angle(to_tm(*mii()))
  radius = fi()
  angle = diff(start, end)

  return radius ** 2 * (angle / 360) * pi


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(f"{t}. {ret:.3f}")
