"""
[33011: 홀수와 짝수 게임](https://www.acmicpc.net/problem/33011)

Tier: Silver 3 
Category: game_theory
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

# P1, P2
# amsminn, heeda0528
def solve():
  n = ii()
  l = mii()
  
  odd = 0
  even = 0
  
  for i in l:
    if i % 2 == 0:
      even += 1
    else:
      odd += 1
  
  if odd == even:
    return "heeda0528"

  mx = max(odd, even)
  
  if mx % 2 == 1:
    return "amsminn"

  return "heeda0528"


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(ret)
