"""
[7131: Õhne vanaraamatupood](https://www.acmicpc.net/problem/7131)

Tier: Bronze 2 
Category: implementation, simulation
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
  N, p0, T = isplit()
  N = int(N)
  p0 = float(p0)
  T = int(T)

  l = [isplit() for _ in range(N)]
  prices = [0] * (N)
  cnt = 1
  prices[0] = p0

  for i in range(1, T):
    avg = sum(prices) / cnt if cnt > 0 else 0

    for idx in range(N):
      start_date, interval, margin_rate = l[idx]
      start_date = int(start_date)
      interval = int(interval)
      margin_rate = float(margin_rate)

      if i >= start_date and (i - start_date) % interval == 0:
        if prices[idx] == 0:
          cnt += 1
        
        prices[idx] = round(avg * (1 + margin_rate), 2)
  
  for price in prices:
    print(f"{price:.2f}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
