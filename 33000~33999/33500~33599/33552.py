"""
[33552: Excellent Grades](https://www.acmicpc.net/problem/33552)

Tier: Bronze 1 
Category: math
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
def round_up_half(n): return floor(n + 0.5, 1)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  last_weight = ii()
  n = ii()

  total_weight = last_weight
  l = [mfi() for _ in range(n)]
  for i in range(n):
    total_weight += l[i][1]
    if l[i][0] < 5.8:
      return "IMPOSSIBLE"
  
  total_score = sum([x[0] * x[1] for x in l])


  a = (8 * (total_weight) - total_score)
  b = last_weight
  x = a / b

  if (x - int(x * 100 / 100)) > 0:
    x = (int((x + 0.1) * 10) / 10)
  else:
    x = (int(x * 10) / 10)
  
  if x > 10.0:
    return "IMPOSSIBLE"

  x = max(x, 5.8)

  return f"{x:.1f}"


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    print(ret)
