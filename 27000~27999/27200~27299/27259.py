"""
[27259: Разноцветные диагонали](https://www.acmicpc.net/problem/27259)

Tier: Bronze 1 
Category: bruteforcing, implementation, math
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
  n = ii()
  l = [[float('inf')] * n for _ in range(n)]

  q = []

  for i in range(n):
    q.append([i, i, 0])
    q.append([i, n - i - 1, 0])

  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]
  while q:
    y, x, d = q.pop(0)

    if l[y][x] <= d:
      continue

    l[y][x] = d

    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]

      if ny < 0 or nx < 0 or ny >= n or nx >= n:
        continue

      if l[ny][nx] <= d + 1:
        continue
      
      q.append([ny, nx, d + 1])

  for i in range(n):
    for j in range(n):
      print(chr(l[i][j] % 26 + ord('a')), end="")
    print()




if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
