"""
[32813: Oooh I See](https://www.acmicpc.net/problem/32813)

Tier: Bronze 1 
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
  n, m = mii()
  l = [inp() for _ in range(n)]

  dy = [0, 1, 0, -1, 1, 1, -1, -1]
  dx = [1, 0, -1, 0, 1, -1, 1, -1]
  cnt = 0
  ans = ()

  for i in range(1, n - 1):
    for j in range(1, m - 1):
      if l[i][j] == "0":        
        if all(l[i + dy[k]][j + dx[k]] == "O" for k in range(8)):
          cnt += 1
          ans = (i + 1, j + 1)
  
  if cnt == 1:
    p(*ans)
  elif cnt > 1:
    p(f"Oh no! {cnt} locations")
  else:
    p("Oh no!")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
