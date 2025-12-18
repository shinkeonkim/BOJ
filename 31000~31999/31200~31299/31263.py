"""
[31263: 대한민국을 지키는 가장 긴 힘](https://www.acmicpc.net/problem/31263)

Tier: Silver 3 
Category: dp, greedy
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
  l = [0] + [*map(int, list(input()))]

  d = [float('inf')] * (n + 1)

  d[0] = 0
  d[1] = 1

  for i in range(2, n + 1):
    if l[i] != 0:
      d[i] = min(d[i], d[i - 1] + 1)
    if i > 1 and l[i - 1] != 0:
      d[i] = min(d[i], d[i - 2] + 1)
    if i > 2 and l[i - 2] != 0 and l[i - 2] * 100 + l[i - 1] * 10 + l[i] <= 641:
      d[i] = min(d[i], d[i - 3] + 1)
  
  print(d[-1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
