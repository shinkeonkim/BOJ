"""
[3213: 피자](https://www.acmicpc.net/problem/3213)

Tier: Silver 4 
Category: math, greedy
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
  n = ii()
  l = [0] * 3
  h = {"1/2": 0, "3/4": 1, "1/4": 2}
  for _ in range(n):
    l[h[input()]] += 1

  half, three_quarter, one_quarter = l
    
  
  # half 처리
  cnt = 0
  cnt += half // 2
  half %= 2
  
  if half > 0:
    for _ in range(2):
      if one_quarter > 0:
        one_quarter -= 1
    
    cnt += 1
  
  k = min(three_quarter, one_quarter)
  cnt += three_quarter
  one_quarter -= k
  
  cnt += (one_quarter) // 4 + (one_quarter % 4 > 0)
  print(cnt)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
