"""
[33524: blobnom.xyz](https://www.acmicpc.net/problem/33524)

Tier: Silver 3 
Category: math, sorting, binary_search
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


def less_counting(l, k):
  cnt = 0
  
  left = 0
  right = len(l) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if l[mid] <= k:
      cnt = max(cnt, mid + 1)
      left = mid + 1
    else:
      right = mid - 1
  
  return cnt

def mx_grid(cnt):
  ans = 0
  left = 0
  right = 1000000000000
  
  while left <= right:
    mid = (left + right) // 2
    
    k = 3 * mid * (mid - 1) + 1
    
    if k <= cnt:
      ans = max(ans, mid)
      left = mid + 1
    else:
      right = mid - 1
  return ans


def solve():
  N, M = mii()
  difficulties = sorted([*map(int, input().split())])
  levels = [*map(int, input().split())]
  
  print(*[mx_grid(less_counting(difficulties, level)) for level in levels])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
