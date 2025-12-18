"""
[9919: Route](https://www.acmicpc.net/problem/9919)

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

def stat(a, b):
  if a == b:
    return 0
  elif a < b:
    return 1
  else:
    return 2

def solve():
  n = int(input())
  l = [int(input()) for _ in range(n)]
  l = l + [l[0]]
  
  stats = []
  current = stat(l[0], l[1])
  current_count = 1
  
  for i in range(1, n):
    next_stat = stat(l[i], l[i + 1])
    if next_stat == current:
      continue

    stats.append(current)
    current = next_stat

  stats.append(current)

  unique_group_stats = [stats[0]]
  
  for i in range(1, len(stats)):
    if stats[i] != stats[i-1]:
      unique_group_stats.append(stats[i])
  
  # if unique_group_stats[-1] == unique_group_stats[0] and len(unique_group_stats) > 1:
  #   unique_group_stats.pop()

  count = Counter(unique_group_stats)
  
  for i in range(3):
    print(count[i], end=' ')

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
