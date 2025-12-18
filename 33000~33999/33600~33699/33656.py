"""
[33656: Island Exploration](https://www.acmicpc.net/problem/33656)

Tier: Silver 2 
Category: graphs, graph_traversal, bfs, dfs, grid_graph, flood_fill
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
  n, m = mii()

  grid = [input() for _ in range(n)]

  cnt = 0

  start = ()

  for i in range(n):
    for j in range(m):
      if grid[i][j] == 'S':
        start = (i, j)
  
  queue = deque([start])
  visited = [[False] * m for _ in range(n)]
  dy = [1, -1, 0, 0]
  dx = [0, 0, 1, -1]

  while queue:
    front = queue.popleft()
    y, x = front
    
    if visited[y][x]:
      continue

    visited[y][x] = True
    cnt += 1

    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]

      if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
      
      if grid[ny][nx] == '.':
        continue

      queue.append((ny, nx))

  print(cnt)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
