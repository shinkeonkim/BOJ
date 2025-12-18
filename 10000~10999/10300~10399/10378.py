"""
[10378: Grave](https://www.acmicpc.net/problem/10378)

Tier: Silver 4 
Category: geometry
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
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  yard = mii()
  chapel = mii()
  w, h = mii()

  total_width = yard[2] - yard[0]
  total_height = yard[3] - yard[1]

  left_width = chapel[0] - yard[0]
  right_width = yard[2] - chapel[2]

  top_height = yard[3] - chapel[3]
  bottom_height = chapel[1] - yard[1]

  if w <= total_width and (h <= top_height or h <= bottom_height):
    return True
  
  if h <= total_height and (w <= left_width or w <= right_width):
    return True
  
  return False


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

    print("Yes" if ret else "No")
