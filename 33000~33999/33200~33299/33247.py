"""
[33247: Alternative Blockchain Algorithms](https://www.acmicpc.net/problem/33247)

Tier: Bronze 2 
Category: arithmetic, implementation, math
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
  chain = [mii() for _ in range(n)]

  if chain[0][1] != 0:
    return (False, "INVALID")
  
  current = chain[0][2]

  if current < 0:
    return (False, "NO_MONEY")

  for i in range(1, n):
    parent_id = chain[i - 1][0]

    if chain[i][1] != parent_id:
      return (False, "INVALID")

    current += chain[i][2]

    if current < 0:
      return (False, "NO_MONEY")

  return (True, current)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    stat, ret = solve()

    if stat:
      print(ret)
    else:
      print(ret)
