"""
[25776: Pseudo Pseudo Random Numbers](https://www.acmicpc.net/problem/25776)

Tier: Silver 4 
Category: bitmask, bruteforcing
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
  N, K = mii()

  l = [[[0] * 2 for _ in range(K + 1)] for _ in range(N + 1)]
  # l[i][j][k] = i번째 수까지 고려했을 때, k라는 숫자가 j 만큼 연속되어있다.

  l[1][1][0] = 1
  l[1][1][1] = 1

  for i in range(2, N + 1):
    for zz in range(0, K + 1):
      l[i][1][1] += l[i - 1][zz][0]
      l[i][1][0] += l[i - 1][zz][1]
    
    for j in range(2, K + 1):
      l[i][j][0] += l[i - 1][j - 1][0]
      l[i][j][1] += l[i - 1][j - 1][1]

  ans = 0
  ans += sum(l[N][j][0] for j in range(1, K + 1))
  ans += sum(l[N][j][1] for j in range(1, K + 1))
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
