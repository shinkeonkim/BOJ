"""
[33080: Party Medley](https://www.acmicpc.net/problem/33080)

Tier: Bronze 2 
Category: arithmetic, bruteforcing, math
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
  l = mii()
  mx = 0
  cnt = 0

  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):

        a =[l[i], l[j], l[k]]

        if max(a) - min(a) <= m:
          cnt += 1
          mx = max(mx, sum(a))
  
  if cnt == 0:
    print(-1)
  else:
    print(cnt, mx)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
