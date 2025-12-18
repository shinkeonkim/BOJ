"""
[34429: Late Larry](https://www.acmicpc.net/problem/34429)

Tier: Bronze 3 
Category: math, implementation, arithmetic
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
  s = input()
  tm, d = s.split()
  h, m = map(int, tm.split(':'))
  minus = ii()
  
  h %= 12
  
  ret = 0
  if d == 'PM':
    ret += 12 * 60
  
  ret += h * 60 + m
  ret -= minus
  
  ret += 24 * 60
  ret %= (24 * 60)

  am_pm = 'AM' if ret < 12 * 60 else 'PM'
  
  h = (ret // 60) % 12
  m = ret % 60
  
  print(f"{h if h != 0 else 12}:{m:02} {am_pm}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
