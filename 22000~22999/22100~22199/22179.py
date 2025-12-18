"""
[22179: Загранпаспорт](https://www.acmicpc.net/problem/22179)

Tier: Bronze 1 
Category: arithmetic, implementation, math, simulation
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

def tm_to_num(tm: str) -> int:
  h, m = map(int, tm.split(":"))
  return h * 60 + m

def solve():
  current = tm_to_num(inp())

  n  = ii()

  for _ in range(n):
    a, b, duration = isplit()
    a = tm_to_num(a)
    b = tm_to_num(b)
    duration = int(duration)

    if current < b and b - max(current, a) >= duration:
      current = max(current, a) + duration
    else:
      return (False, -1)
  
  return (True, current)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

    if ret[0]:
      p("Yes")
      p(f"{ret[1] // 60:02}:{ret[1] % 60:02}")
    else:
      p("No")
    
