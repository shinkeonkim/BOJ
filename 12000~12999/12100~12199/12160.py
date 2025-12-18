"""
[12160: Mushroom Monster (Small)](https://www.acmicpc.net/problem/12160)

Tier: Silver 3 
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
  n = ii()
  l = mii()

  ans = [0, 0]

  mn = 0

  crt = l[0]

  for i in l[1:]:
    if crt >= i:
      mn += crt - i
    crt = i
  
  ans[0] = mn

  diff_mx = 0

  for i in range(1, n):
    if l[i - 1] < l[i]:
      continue
    diff_mx = max(diff_mx, l[i - 1] - l[i])
  

  for i in range(0, n - 1):
    ans[1] += min(diff_mx, l[i])
  
  return ans

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret[0]} {ret[1]}")
