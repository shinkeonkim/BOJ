"""
[21402: Фитнесс-клуб](https://www.acmicpc.net/problem/21402)

Tier: Bronze 1 
Category: greedy
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
  n, k = mii()

  l = [mii() for _ in range(n)]

  locked = k
  opened = 0

  for end_lock, end_open in l:
    if end_lock > locked:
      over_lock = end_lock - locked
      locked += over_lock
      opened -= over_lock
    elif end_lock < locked:
      left_lock = locked - end_lock
      opened += min(left_lock, end_open)
      locked -= min(left_lock, end_open)

  print(opened)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
