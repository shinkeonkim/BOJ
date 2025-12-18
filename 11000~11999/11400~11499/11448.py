"""
[11448: Ga](https://www.acmicpc.net/problem/11448)

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
def round_up_half(n): return floor(n + 0.5)


def solve():
  n = ii()
  grid = [input() for _ in range(n)]
  is_visited = [[False] * n for _ in range(n)]

  dy = [0, 1, 0, -1, 1, 1, -1, -1]
  dx = [1, 0, -1, 0, 1, -1, -1, 1]

  queue = deque()
  ans = 0

  for i in range(n):
    for j in range(n):
      if grid[i][j] == 'w':
        queue.append((i, j))
  
  while queue:
    y, x = queue.popleft()

    if is_visited[y][x]:
      continue

    if grid[y][x] == '-':
      ans += 1
    is_visited[y][x] = True

    for d in range(8):
      ny, nx = y + dy[d], x + dx[d]

      if ny < 0 or ny >= n or nx < 0 or nx >= n:
        continue

      if grid[ny][nx] != '-':
        continue

      queue.append((ny, nx))
  
  print(ans)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
