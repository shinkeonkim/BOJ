"""
[9620: Meeting Room Arrangement](https://www.acmicpc.net/problem/9620)

Tier: Silver 2 
Category: greedy, sorting
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
def round_up_half(n): return floor(n + 0.5)


def solve():
  l = []
  while 1:
    a, b = mii()

    if a == b == 0:
      break

    l.append((a, b))

  l.sort(key=lambda x: (x[1], x[0]))

  ans = 1
  prev = l[0][1]

  for i in range(1, len(l)):
    start, end = l[i]

    if prev > start:
      continue

    ans += 1
    prev = end
  
  print(ans)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
