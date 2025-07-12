"""
[29292: X частей](https://www.acmicpc.net/problem/29292)

Tier: Bronze 2 
Category: arithmetic, greedy, math
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
  N, X = mii()
  A = mii()
  B = mii()

  ans = 0 # diff sum
  current_sum = 0

  g = 0
  for i in range(N):
    current_sum += A[i]

    if current_sum >= B[g]:
      ans += current_sum - B[g]
      current_sum = 0
      g += 1
    
    if g >= X:
      for j in range(i + 1, N):
        ans += A[j]
      break
  
  if g < X:
    print(-1)
  else:
    print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()