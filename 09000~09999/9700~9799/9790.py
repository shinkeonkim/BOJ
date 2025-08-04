"""
[9790: Elephant Show](https://www.acmicpc.net/problem/9790)

Tier: Silver 2 
Category: bfs, dfs, graphs, graph_traversal
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


def solve(w, h):
  grid = [input() for _ in range(h)]
  visited = [[False] * w for _ in range(h)]

  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]

  start = ()

  for i in range(h):
    for j in range(w):
      if grid[i][j] == 'A':
        start = (i, j)
        break
    if start:
      break
  
  queue = deque([start])
  ans = 0

  while queue:
    here = queue.popleft()
    y, x = here

    if visited[y][x]: continue

    visited[y][x] = True
    ans += 1

    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]

      if ny < 0 or nx < 0 or ny >= h or nx >= w: continue
      if grid[ny][nx] != '.': continue
      if visited[ny][nx]: continue

      queue.append((ny, nx))
  
  print(ans)


if __name__ == "__main__":
  while 1:
    w, h = mii()
    if w == h == 0:
      break
    solve(w, h)