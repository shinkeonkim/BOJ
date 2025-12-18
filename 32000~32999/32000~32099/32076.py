"""
[32076: Easy as ABC](https://www.acmicpc.net/problem/32076)

Tier: Silver 4 
Category: implementation, string, bruteforcing
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
  l = [input() for _ in range(3)]

  dy = [1, 0, -1, 0, 1, 1, -1, -1]
  dx = [0, 1, 0, -1, 1, -1, 1, -1]
  chk = [[False] * 3 for _ in range(3)]

  st = set()

  def dfs(y, x, crt):
    if len(crt) == 3:
      st.add(crt)
      return

    for i in range(8):
      ny, nx = y + dy[i], x + dx[i]
      
      if ny < 0 or ny >= 3 or nx < 0 or nx >= 3 or chk[ny][nx]:
        continue

      chk[ny][nx] = True
      dfs(ny, nx, crt + l[ny][nx])
      chk[ny][nx] = False
  
  for i in range(3):
    for j in range(3):
      chk[i][j] = True
      dfs(i, j, l[i][j])
      chk[i][j] = False
  
  print(sorted(st)[0])

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
