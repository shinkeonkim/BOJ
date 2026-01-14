"""
[14921: 용액 합성하기](https://www.acmicpc.net/problem/14921)

Tier: Gold 5 
Category: two_pointer
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
from fractions import Fraction

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
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  n = ii()
  l = mii()
  
  l.sort()
  ans = float('inf')
  mn_diff = float('inf')
  
  for i in range(n):
    crt = l[i]
    target = -crt
    
    left = max(0, bisect_left(l, target) - 200)
    right = min(bisect_right(l, target) + 200, n)
    
    for nxt_idx in range(left, right):
      if i == nxt_idx:
        continue
      
      diff = abs(crt + l[nxt_idx])
      
      if diff < mn_diff:
        mn_diff = diff
        ans = crt + l[nxt_idx]
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
