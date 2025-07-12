"""
[29627: Ноутбук](https://www.acmicpc.net/problem/29627)

Tier: Bronze 2 
Category: arithmetic, implementation, math
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
  n, x, y = mii() # x: 방전에 걸리는 시간, y: 충전에 걸리는 시간

  prev = 0
  stat = 0 # 0: 충전 중, 1: 충전 X
  battery = 100

  times = [[*map(int, inp().split(":"))] for _ in range(n)] + [(23, 59)]

  for i in range(n+1):
    tm = times[i][0] * 60 + times[i][1]
    duration = tm - prev

    if stat == 0:
      battery += duration * (100 / y)
      if battery > 100:
        battery = 100
    else:
      battery -= duration * (100 / x)
      if battery < 0:
        battery = 0

    prev = tm
    stat = 1 - stat

  
  print(f"{battery:.3f}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
