"""
[4749: Take Your Vitamins](https://www.acmicpc.net/problem/4749)

Tier: Bronze 1 
Category: arithmetic, implementation, math, parsing, string
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


def solve():
  no_significant_amount = []
  
  while 1:
    A, U, R, *V = isplit()
    A = float(A)
    R = float(R)
    V = " ".join(V)
    
    if A < 0:
      break
    
    rate = round_up_half(A / R * 100)

    if A * 100 < R:
      no_significant_amount.append(V)
    else:
      print(V, f"{A:.1f}", U, f"{rate}%")

  if no_significant_amount:
    print("Provides no significant amount of:")
  print(*no_significant_amount, sep="\n")


if __name__ == "__main__":
  solve()