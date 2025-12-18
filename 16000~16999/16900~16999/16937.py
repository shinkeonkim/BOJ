"""
[16937: 두 스티커](https://www.acmicpc.net/problem/16937)

Tier: Silver 3 
Category: implementation, bruteforcing, geometry, case_work
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

def get_area(sticker):
  return sticker[0] * sticker[1]

def comp(s1, s2, H, W):
  return s1[0] + s2[0] <= H and max(s1[1], s2[1]) <= W

def is_available(s1, s2, H, W):
  if comp(s1, s2, H, W) or comp(s1, s2, W, H):
    return True
  
  s1 = s1[::-1]
  if comp(s1, s2, H, W) or comp(s1, s2, W, H):
    return True
  
  s2 = s2[::-1]
  if comp(s1, s2, H, W) or comp(s1, s2, W, H):
    return True

  s1 = s1[::-1]
  if comp(s1, s2, H, W) or comp(s1, s2, W, H):
    return True

  return False

def solve():
  H, W = mii()
  N = ii()
  stickers = [mii() for _ in range(N)]
  
  mx = 0
  
  for i in range(N):
    for j in range(i + 1, N):
      if is_available(stickers[i], stickers[j], H, W):
        mx = max(mx, get_area(stickers[i]) + get_area(stickers[j]))

  print(mx)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
