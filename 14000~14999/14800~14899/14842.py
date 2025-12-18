"""
[14842: 재홍의 사다리](https://www.acmicpc.net/problem/14842)

Tier: Silver 5 
Category: math, geometry
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
  W, H, N = mii()

  i = 1
  ans = 0

  while 2 * H * i <= H * N:
    k =H - 2 *  H * i / N
    if 2 * H * i < H * N:
      ans += k
    ans += k
    i += 1
  
  print(f"{ans:.6f}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
