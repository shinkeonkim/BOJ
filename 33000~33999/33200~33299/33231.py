"""
[33231: Coatis and Owls](https://www.acmicpc.net/problem/33231)

Tier: Bronze 1 
Category: implementation, math, simulation
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
def near_integer(x): return int(x + 0.5) if x >= 0 else int(x - 0.5)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  n, m = mii()
  
  l = mii()
  A = l[:n][::-1]
  B = l[n:]
  
  i = j = 0
  
  while i < n and j < m:
    if A[i] == B[j]:
      A[i] = 0
      B[j] = 0
      i += 1
      j += 1
    elif A[i] < B[j]:
      B[j] -= ceil((A[i] ** 2) / B[j])
      A[i] = 0
      i += 1
      if B[j] == 0:
        j += 1
    else:
      A[i] -= ceil((B[j] ** 2) / A[i])
      B[j] = 0
      j += 1
      if A[i] == 0:
        i += 1


  if i == n and j == m:
    print("stalemate")
  elif j == m:
    print("coatis")
    print(sum(A))
  else:
    print("owls")
    print(sum(B))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
