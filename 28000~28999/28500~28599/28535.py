"""
[28535: Расколбас с Франкенштейном](https://www.acmicpc.net/problem/28535)

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
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  d = "NZQR"
  s = input().split(" ")
  a = s[0]
  b = s[-1]

  a = d.index(a)
  b = d.index(b)
  oper = s[1]

  if a == b == 0 and oper == '-':
    print("Z")
    return

  if a == b == 3 and oper == '*':
    print("R")
    return

  assert (0 <= a <= 3)
  assert (0 <= b <= 3)

  print(d[max(a, b)])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
