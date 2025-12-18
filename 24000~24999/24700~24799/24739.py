"""
[24739: Sequinary Numerals](https://www.acmicpc.net/problem/24739)

Tier: Silver 5 
Category: arithmetic, euclidean, implementation, math, number_theory, string
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

def solve():
  l = [*map(int, list(inp()))]

  ans = Fraction(0, 1)

  for i in range(len(l)):
    ans += Fraction(l[i], 1) * Fraction(3, 2) ** (len(l) - i - 1)

  dominator = ans.denominator
  numerator = ans.numerator

  ret = ""
  if numerator == 0:
    ret = "0"
  else:
    natural = numerator // dominator

    if natural:
      ret += f"{natural} "

    if dominator != 1:
      ret += f"{numerator % dominator}/{dominator}"

  print(ret)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
