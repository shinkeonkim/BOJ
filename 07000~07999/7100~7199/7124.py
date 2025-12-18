"""
[7124: Sarnased kolmnurgad](https://www.acmicpc.net/problem/7124)

Tier: Bronze 1 
Category: geometry, pythagoras
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


def f(l: list):
  ret = []
  for i in range(3):
    x, y = l[2 * i], l[2 * i + 1]
    nx, ny = l[(2 * (i + 1)) % 6], l[(2 * (i + 1)) % 6 + 1]

    ret.append((x - nx) ** 2 + (y - ny) ** 2)
  
  return sorted(ret)

def similar_rate(A: list, B: list):
  # print(A, B)
  if A[0] * B[1] == A[1] * B[0] and A[1] * B[2] == A[2] * B[1]:
    return sqrt(A[0] / B[0])

  return -1

def solve():
  A = mii()
  B = mii()

  A = f(A)
  B = f(B)

  print(similar_rate(A, B))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
