"""
[22810: When Can We Meet?](https://www.acmicpc.net/problem/22810)

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


def solve(N, Q):
  l = []
  
  counter = Counter()
  
  for _ in range(N):
    z, *days = mii()
    
    for day in days:
      counter[day] += 1

  mx = max(counter.values() or [0])

  if mx < Q:
    print(0)
    return
  
  for k, v in sorted(counter.items()):
    if v == mx:
      print(k)
      return


if __name__ == "__main__":
  while 1:
    N, Q = map(int, input().split())
    if N == Q == 0:
      break
    
    solve(N, Q)