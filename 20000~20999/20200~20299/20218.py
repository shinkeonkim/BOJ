"""
[20218: Figure Skating](https://www.acmicpc.net/problem/20218)

Tier: Bronze 1 
Category: implementation, string
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
  expected = {}

  for i in range(1, n + 1):
    s = inp()
    expected[s] = n - i + 1
  
  actual = {}
  for i in range(1, n + 1):
    s = inp()
    actual[s] = n - i + 1
  
  ans = ""
  mx = 0
  score = 0

  for s in expected:
    expected_score = expected[s]
    actual_score = actual[s]

    if expected_score < actual_score:
      if mx < actual_score - expected_score:
        ans = s
        mx = actual_score - expected_score
        score = actual_score
      elif mx == actual_score - expected_score:
        if score < actual_score:
          ans = s
          score = actual_score
  
  print(ans if ans else "suspicious")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
