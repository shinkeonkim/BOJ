"""
[11497: 통나무 건너뛰기](https://www.acmicpc.net/problem/11497)

Tier: Silver 1 
Category: greedy, sorting
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
  l = sorted(mii())
  ans = []
  for i in range(0, n, 2):
    ans.append(l[i])
  
  for i in range(n-1-(n%2), 0, -2):
    ans.append(l[i])
  
  mx_diff = 0
  
  for i in range(0, n):
    mx_diff = max(mx_diff, abs(ans[i] - ans[i-1]))

  print(mx_diff)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
