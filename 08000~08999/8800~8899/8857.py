"""
[8857: Kodowanie](https://www.acmicpc.net/problem/8857)

Tier: Silver 3 
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

d = [[0, 0] for _ in range(55)]

def dp():
  # d[i][j] = j로 끝나면서, 지금까지 연속된 11이 없는 길이

  d[1][0] = 0
  d[1][1] = 1

  for i in range(2, 55):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]

def solve():
  n = ii()
  ans = d[n][0] + d[n][1]
  return ans
  


if __name__ == "__main__":
  tc = ii()
  dp()
  for t in range(1, tc+1):
    ret = solve()
    print(ret)
