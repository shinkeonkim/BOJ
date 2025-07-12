"""
[19858: Золотые слитки](https://www.acmicpc.net/problem/19858)

Tier: Bronze 2 
Category: ad_hoc, case_work, constructive, math
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
  l = mii()

  if sum(l) == 2 * max(l):
    print(0)
    return

  a, b, c = sorted(l)

  if (a + b + c) % 2 != 0:
    print(-1)
    return

  target = (a + b + c) // 2

  if 2 * target - a - b != c:
    print(-1)
    return

  print(l.index(c) + 1)
  print(target - a, target - b)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
