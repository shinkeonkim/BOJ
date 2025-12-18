"""
[29087: Смех, да и только!](https://www.acmicpc.net/problem/29087)

Tier: Bronze 1 
Category: implementation, dp, greedy, string
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

  s = inp()

  last = ""
  mx = 0
  cnt = 0

  for i in s:
    if i == 'a':
      if last == 'a' or last == '':
        cnt = 1
      elif last == 'h':
        cnt += 1
      last = 'a'
    elif i == 'h':
      if last == 'h' or last == '':
        cnt = 1
      elif last == 'a':
        cnt += 1
      last = 'h'
    else:
      last = ''
      cnt = 0

    mx = max(mx, cnt)
  
  print(mx)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
