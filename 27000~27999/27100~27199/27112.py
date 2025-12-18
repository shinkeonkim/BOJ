"""
[27112: 시간 외 근무 멈춰!](https://www.acmicpc.net/problem/27112)

Tier: Silver 2 
Category: greedy, sorting
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
MAX_DAY = 100001

def solve():
  n = ii()
  l = [mii() for _ in range(n)]

  need_works = [[] for _ in range(MAX_DAY)]
  
  mx_day = 0

  for a, b in l:
    need_works[a].append(b)
    mx_day = max(mx_day, a)
  
  ans = 0
  is_possible = True
  
  current_normal = 0
  current_extra = 0
  used_extra = 0
  
  for i in range(1, mx_day+1):
    if i % 7 == 0 or i % 7 == 6:
      current_extra += 1
    else:
      current_normal += 1
      current_extra += 1

    have_to = need_works[i]
    # print(i, "day: ", current_extra, current_normal, have_to)

    if have_to:
      if sum(have_to) > current_extra + current_normal:
        is_possible = False
        break
      
      for work in have_to:
        if current_normal >= work:
          current_normal -= work
        else:
          work -= current_normal
          current_normal = 0
          current_extra -= work
          used_extra += work
  
  if is_possible:
    print(used_extra)
  else:
    print(-1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
