"""
[29640: Кёрлинг](https://www.acmicpc.net/problem/29640)

Tier: Bronze 1 
Category: implementation, math, sorting
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

def f(l):
  return [l[0] ** 2 + l[1] ** 2, l[0], l[1]]

def solve():
  n = ii()
  score = {'A': 0, 'B': 0}

  for _ in range(n):
    m, k = mii()

    A = [f(mii()) for _ in range(m)]
    B = [f(mii()) for _ in range(k)]

    A.sort()
    B.sort()

    if A[0][0] < B[0][0]:
      cnt = 0
      for i in range(m):
        if A[i][0] < B[0][0]:
          cnt += 1
      score['A'] += cnt
    elif A[0][0] > B[0][0]:
      cnt = 0
      for i in range(k):
        if B[i][0] < A[0][0]:
          cnt += 1
      score['B'] += cnt 
    else:
      continue
  
  print(f"{score['A']}:{score['B']}")
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
