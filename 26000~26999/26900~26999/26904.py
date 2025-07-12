"""
[26904: Tågväxeln](https://www.acmicpc.net/problem/26904)

Tier: Bronze 2 
Category: arithmetic, implementation, math, simulation
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

  switch = 0 if n < m else 1

  ans = 0

  for i in range(1, 1440):
    if i % n == 0 and i % m == 0:
      switch = 1 - switch
      ans += 1
    elif i % n == 0:
      if switch == 1:
        switch = 0
        ans += 1
        # print(i, "1 - > 0")
    elif i % m == 0:
      if switch == 0:
        switch = 1
        ans += 1
        # print(i, "0 - > 1")

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
