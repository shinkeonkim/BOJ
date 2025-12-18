"""
[5929: Awkward Digits](https://www.acmicpc.net/problem/5929)

Tier: Silver 5 
Category: bruteforcing, implementation, math, string
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

def join(a: list) -> str:
  return "".join(map(str, a))

def solve():
  A = [*map(int, list(inp()))]
  B = [*map(int, list(inp()))]
  
  A2 = set()
  B2 = set()
  A2.add(int(join(A), 2))
  B2.add(int(join(B), 3))
  
  for i in range(len(A)):
    A[i] = 1 - A[i]
    A2.add(int(join(A), 2))
    A[i] = 1 - A[i]
  
  for i in range(len(B)):
    B[i] = (B[i] + 1) % 3
    B2.add(int(join(B), 3))
    B[i] = (B[i] + 1) % 3
    B2.add(int(join(B), 3))
    B[i] = (B[i] + 1) % 3

  print(*(A2 & B2))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
