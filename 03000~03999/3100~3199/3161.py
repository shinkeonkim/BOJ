"""
[3161: izbori](https://www.acmicpc.net/problem/3161)

Tier: Silver 3 
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
  M, N = mii()

  l = [mii() for _ in range(M)]

  win_count = defaultdict(lambda: 0)

  for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
      i_wins = 0
      j_wins = 0
      for k in range(M):
        if l[k].index(i) < l[k].index(j):
          i_wins += 1
        else:
          j_wins += 1
      
      if i_wins > j_wins:
        win_count[i] += 1
      elif j_wins > i_wins:
        win_count[j] += 1

  mx = max(win_count.values())

  for i in range(1, N + 1):
    if win_count[i] == mx:
      p(i)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
