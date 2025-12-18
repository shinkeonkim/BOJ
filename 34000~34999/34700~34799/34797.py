"""
[34797: GPA Computation](https://www.acmicpc.net/problem/34797)

Tier: Bronze 3 
Category: math, implementation, string, arithmetic
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

def f(s):
  d = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
  
  score = d[s[0]]
  add = {'1': 0.05, '2': 0.025, '3': 0}[s[1]] if score >= 2 else 0
  
  return score, add

def solve():
  n = ii()
  
  sm1, sm2 = 0, 0
  for _ in range(n):
    score, add = f(inp())
    sm1 += score
    sm2 += add
  
  print(f"{sm1 / n + sm2:.6f}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
