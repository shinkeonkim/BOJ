"""
[11611: Blur](https://www.acmicpc.net/problem/11611)

Tier: Silver 2 
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

def transform(l, n, m):
  ret = [[0] * m for _ in range(n)]

  dy = [0, 0, 0, 1, -1, 1, 1, -1, -1]
  dx = [0, 1, -1, 0, 0, 1, -1, 1, -1]
  for i in range(n):
    for j in range(m):
      for d in range(len(dy)):
        ny = (i + dy[d] + n) % n
        nx = (j + dx[d] + m) % m
        
        ret[i][j] += l[ny][nx]
  return ret

def solve():
  m, n, k = map(int, input().split())
  
  l = [[*map(int, input().split())] for _ in range(n)]
  
  st = set()
  for _ in range(k):
    l = transform(l, n, m)

  for i in l:
    for j in i:
      st.add(j)
  
  print(len(st))  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
