"""
[9781: Knight Moves](https://www.acmicpc.net/problem/9781)

Tier: Silver 1 
Category: graphs, graph_traversal, bfs
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
  n, m = mii()
  
  grid = [input() for _ in range(n)]
  chk = [[float('inf')] * m for _ in range(n)]
  
  start = None
  destination = None
  
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 'K':
        start = (i, j, 0)
      
      if grid[i][j] == 'X':
        destination = (i, j)
  
  queue = deque([start])
  dx = [2, 2, -2, -2, 1, 1, -1, -1]
  dy = [1, -1, 1, -1, 2, -2, -2, -2]

  while queue:
    y, x, cost = queue.popleft()
    
    if cost >= chk[y][x]:
      continue
    
    chk[y][x] = cost
    
    for d in range(8):
      ny, nx = y + dy[d], x + dx[d]
      
      if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
      
      if grid[ny][nx] == '#':
        continue

      if chk[ny][nx] > cost + 1:
        queue.append((ny, nx, cost + 1))
  
  # print(*chk, sep='\n')
  dis = chk[destination[0]][destination[1]]
  print(dis if dis != float('inf') else -1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
