"""
[32344: 유물 발굴](https://www.acmicpc.net/problem/32344)

Tier: Silver 5 
Category: implementation, geometry, set
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


def solve():
  R, C = mii()
  N = ii()
  
  d = defaultdict(lambda : (float('inf'), 0, float('inf'), 0))
  
  for _ in range(N):
    num, y, x = mii()
    
    current = d[num]
    nxt = (min(current[0], y), max(current[1], y), min(current[2], x), max(current[3], x))
    d[num] = nxt
  
  sz = defaultdict(int)
  
  for k, v in d.items():
    sz[k] = (v[1] - v[0] + 1) * (v[3] - v[2] + 1)
  
  sz = sorted(sz.items(), key=lambda x : (-x[1], x[0]))
  
  print(*sz[0])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
