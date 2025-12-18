"""
[28825: Фоторобот Грин-де-Вальда](https://www.acmicpc.net/problem/28825)

Tier: Bronze 1 
Category: bitmask, implementation
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

def is_available(color: str, permission: str) -> bool:
  permission = int(permission)

  if permission == 0:
    return color == "."

  avaiable_set = ["." ]

  if permission & 1:
    avaiable_set.append("R")
  if permission & 2:
    avaiable_set.append("G")
  if permission & 4:
    avaiable_set.append("B")

  return color in avaiable_set

def solve():
  n, m = mii()
  colors = [inp() for _ in range(n)]
  permissions = [inp() for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if is_available(colors[i][j], permissions[i][j]):
        continue
      print("incorrect")
      return
  print("correct")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
