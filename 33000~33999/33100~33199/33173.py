"""
[33173: マスキングテープ (Masking Tape)](https://www.acmicpc.net/problem/33173)

Tier: Bronze 2 
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
  H, W, Q = mii()

  cells = [[0] * W for _ in range(H)]
  masking = [[False] * W for _ in range(H)]

  for _ in range(Q):
    query = mii()

    if query[0] == 1:
      # 색깔을 칠하는 쿼리

      for i in range(query[1] - 1, query[1] + 1):
        for j in range(query[2] - 1, query[2] + 1):
          if not masking[i][j]:
            cells[i][j] = query[3]
    else:
      # 마스킹하는 쿼리
      for i in range(query[1] - 1, query[1] + 1):
        for j in range(query[2] - 1, query[2] + 1):
          masking[i][j] = True
  
  # 모든 색상 출력

  for i in range(H):
    print(*cells[i])

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
