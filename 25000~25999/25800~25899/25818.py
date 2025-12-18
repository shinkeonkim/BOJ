"""
[25818: How Much Coffee is Left?](https://www.acmicpc.net/problem/25818)

Tier: Silver 4 
Category: math, geometry, geometry_3d
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

def truncated_cone_volume(r, R, H): # 뿔대 부피 (r < R)
  return 1 / 3 * pi * H * (r ** 2 + r * R + R ** 2)


def solve():
  r, s, h, m, d = mii()
  # r: bottom radius
  # s: top radius
  # h: cup height
  # m: 커피를 마신 시간 (분)
  # d: 현재 남아있는 커피의 높이

  # s ~ r
  # h:d = s:coffee_radius

  coffee_radius = d * (s - r) / h + r
  drunk_volume = truncated_cone_volume(coffee_radius, s, h - d)
  left_volume = truncated_cone_volume(r, coffee_radius, d)

  print(left_volume * m / drunk_volume)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
