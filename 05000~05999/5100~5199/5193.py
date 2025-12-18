"""
[5193: Fundraising](https://www.acmicpc.net/problem/5193)

Tier: Bronze 1 
Category: implementation
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
  c, d, t = mii()
  
  personal_d = {}
  total_d = {}
  
  violators = set()
  
  for _ in range(t):
    a, b, m = mii()
    
    personal_d[(a, b)] = personal_d.get((a, b), 0) + m
    
    total_d[a] = total_d.get(a, 0) + m
  
  for (a, b), m in personal_d.items():
    if m > 2100:
      violators.add(a)
  
  for a, m in total_d.items():
    if m > 40000:
      violators.add(a)
  
  return sorted(violators)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Data Set {t}:")
    if ret:
      print("Violators:")
      print(*ret, sep="\n")
    else:
      print("No violations")
