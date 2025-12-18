"""
[27495: 만다라트 만들기](https://www.acmicpc.net/problem/27495)

Tier: Silver 3 
Category: implementation, sorting
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


mandalart = [input().split() for _ in range(9)]

ordering = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

di = defaultdict(list)

for i, (dy, dx) in enumerate(ordering):
  center = (4 + dy * 3, 4 + dx * 3)
  di[mandalart[center[0]][center[1]]] = []
  for j, (ddy, ddx) in enumerate(ordering):
    sub = (center[0] + ddy, center[1] + ddx)

    di[mandalart[center[0]][center[1]]].append(mandalart[sub[0]][sub[1]])

di = sorted(di.items(), key=lambda x: x[0])

for i, (k, v) in enumerate(di):
  v = sorted(v)
  
  print(f"#{i + 1}. {k}")
  for j, vv in enumerate(v):
    print(f"#{i + 1}-{j + 1}. {vv}")
