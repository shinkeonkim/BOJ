"""
[6080: Bad Grass](https://www.acmicpc.net/problem/6080)

Tier: Silver 2 
Category: graphs, graph_traversal, bfs, dfs
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
  q = deque([])
  
  l = [mii() for _ in range(n)]
  chk = [[False] * m for _ in range(n)]
  ans = 0

  dy = [0, 1, 0, -1, 1, 1, -1, -1]
  dx = [1, 0, -1, 0, 1, -1, 1, -1]

  for i in range(n):
    for j in range(m):
      if chk[i][j] or l[i][j] == 0:
        continue
      
      ans += 1

      q.append((i, j))
      chk[i][j] = True
      
      while q:
        y, x = q.popleft()
        
        for d in range(8):
          ny, nx = y + dy[d], x + dx[d]
          
          if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
          
          if chk[ny][nx] or l[ny][nx] == 0:
            continue

          q.append((ny, nx))
          chk[ny][nx] = True

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
