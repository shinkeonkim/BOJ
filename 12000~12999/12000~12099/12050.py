"""
[12050: Dynamic Grid (Small)](https://www.acmicpc.net/problem/12050)

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


def solve():
  n, m = mii()
  grid = [[*map(int, list(inp()))] for _ in range(n)]

  q = ii()
  
  for _ in range(q):
    query = isplit()

    if query[0] == "Q":
      chk = [[0] * m for _ in range(n)]
      cnt = 0

      for i in range(n):
        for j in range(m):
          if grid[i][j] == 0:
            continue
            
          if chk[i][j] == 1:
            continue
          
          cnt += 1
          q = deque([(i, j)])

          while q:
            y, x = q.popleft()
            chk[y][x] = 1

            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
              ny, nx = y + dy, x + dx
              
              if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
              
              if grid[ny][nx] == 0 or chk[ny][nx] == 1:
                continue

              q.append((ny, nx))
      p(cnt)
    else:
      y, x, v = map(int, query[1:])
      grid[y][x] = v


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    print(f"Case #{tc}:")
    ret = solve()
