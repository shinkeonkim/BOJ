"""
[25421: 조건에 맞는 정수의 개수](https://www.acmicpc.net/problem/25421)

Tier: Silver 1 
Category: dp
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

MOD = 987654321

def solve():
  n = ii()

  l = [1] * 10

  l[0] = 0

  for i in range(2, n + 1):
    nxt = [0] * 10

    for j in range(1, 10):
      for k in range(-2, 3):
        if j + k < 0 or j + k >= 10:
          continue

        nxt[j] += l[j + k]
        nxt[j] %= MOD

    l = nxt

  print(sum(l) % MOD)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
