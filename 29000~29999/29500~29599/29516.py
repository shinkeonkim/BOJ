"""
[29516: Королевский сад](https://www.acmicpc.net/problem/29516)

Tier: Bronze 2 
Category: bruteforcing, implementation
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
  a, b = mii()
  l = [inp() for _ in range(a)]

  c = dict()

  for i in l:
    for j in i:
      c[j] = c.get(j, 0) + 1
  
  for i in range(a):
    c2 = c.copy()

    for j in range(b):
      c2[l[i][j]] -= 1

    categories = set(k for k, v in c2.items() if v > 0)

    if len(categories) <= 1:
      return True
  
  for j in range(b):
    c2 = c.copy()
    
    for i in range(a):
      c2[l[i][j]] -= 1

    categories = set(k for k, v in c2.items() if v > 0)
    if len(categories) <= 1:
      return True

  return False      


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

    print("Yes" if ret else "No")
