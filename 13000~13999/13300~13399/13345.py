"""
[13345: Completing the Square](https://www.acmicpc.net/problem/13345)

Tier: Silver 2 
Category: math, geometry
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


def distance_squared(a, b):
  x1, y1 = a
  x2, y2 = b
  return (x1 - x2) ** 2 + (y1 - y2) ** 2

def diff(a, b):
  return (a[0] - b[0]), (a[1] - b[1])

def solve():
  l = [mii() for _ in range(3)]

  center = 0

  for i in range(3):
    if distance_squared(l[i], l[(i + 1) % 3]) == distance_squared(l[i], l[(i + 2) % 3]):
      center = i
      break

  df = diff(l[(center + 1) % 3], l[center])
  print(l[(center + 2) % 3][0] + df[0], l[(center + 2) % 3][1] + df[1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
