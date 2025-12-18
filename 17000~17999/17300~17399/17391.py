"""
[17391: 무한부스터](https://www.acmicpc.net/problem/17391)

Tier: Silver 1 
Category: dp, graphs, graph_traversal, bfs, grid_graph
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

n, m = mii()
l = [mii() for _ in range(n)]
dp = [[float('inf')] * m for _ in range(n)]

q = deque([(0, 0, 0)])

while q:
  y, x, c = q.popleft()
  
  if l[y][x] > 0:
    c += 1
  
  if dp[y][x] <= c:
    continue
  
  dp[y][x] = c
  
  for i in range(y + 1, min(n, y + l[y][x] + 1)):
    if dp[i][x] < c + 1:
      continue
    q.append((i, x, c))
  
  for j in range(x + 1, min(m, x + l[y][x] + 1)):
    if dp[y][j] < c + 1:
      continue
    q.append((y, j, c))
    
print(dp[n - 1][m - 1] - 1)
