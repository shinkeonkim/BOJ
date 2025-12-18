"""
[17587: Gerrymandering](https://www.acmicpc.net/problem/17587)

Tier: Bronze 1 
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
  P, D = mii()
  votes = [[0, 0] for _ in range(D + 1)]
  V = 0

  for i in range(P):
    d, a, b = mii()
    votes[d][0] += a
    votes[d][1] += b
    V += a + b
  
  wasted_sum = [0, 0]

  for i in range(1, D + 1):
    if votes[i][0] > votes[i][1]:
      wasted = votes[i][0] - (sum(votes[i]) // 2 + 1)
      print("A", wasted, votes[i][1])
      wasted_sum[0] += wasted
      wasted_sum[1] += votes[i][1]
    else:
      wasted = votes[i][1] - (sum(votes[i]) // 2 + 1)
      print("B", votes[i][0], wasted)
      wasted_sum[0] += votes[i][0]
      wasted_sum[1] += wasted
  
  print(abs(wasted_sum[0] - wasted_sum[1]) / V)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
