"""
[34002: 임스의 잠수맵](https://www.acmicpc.net/problem/34002)

Tier: Bronze 1 
Category: implementation, greedy, simulation
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


def solve():
  A, B, C = mii()
  S, V = mii()
  L = ii()

  S *= 30
  V *= 30

  need_level = 250 - L

  tm = 0
  count = 0
  while need_level > 0:
    tm += 1
    if V > 0:
      count += C
      V -= 1
    elif S > 0:
      count += B
      S -= 1
    else:
      count += A
    
    if count >= 100:
      need_level -= count // 100
      count %= 100
  print(tm)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
