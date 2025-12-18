"""
[6553: Diplomatic License](https://www.acmicpc.net/problem/6553)

Tier: Bronze 1 
Category: geometry
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

SYS_INPUT = False
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
  while 1:
    try:
      n, *l = mii()
    except EOFError:
      break
    axis = [(l[i], l[i+1]) for i in range(0, len(l), 2)]

    ans = []
    for i in range(n):
      fi = axis[i]
      se = axis[(i + 1) % n]

      ans.append((fi[0] + se[0]) / 2)
      ans.append((fi[1] + se[1]) / 2)

    print(n, end=" ")
    for i in ans:
      print(f"{i:.6f}", end=" ")
    print()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
