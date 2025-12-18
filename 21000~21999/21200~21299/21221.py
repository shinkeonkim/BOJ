"""
[21221: Bold](https://www.acmicpc.net/problem/21221)

Tier: Silver 5 
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
  chk = [[False] * m for _ in range(n)]

  for i in range(n - 1):
    for j in range(m - 1):
      if l[i][j] == '#':
        chk[i][j] = chk[i + 1][j] = chk[i][j + 1] = chk[i + 1][j + 1] = True
  
  for i in range(n):
    for j in range(m):
      print('#' if chk[i][j] else '.', end='')
    print()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
