"""
[34802: 강의실 들어가기](https://www.acmicpc.net/problem/34802)

Tier: Bronze 3 
Category: math, implementation, string, arithmetic, parsing
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
def tm_to_int(tm: str):
  h,m,s = map(int, tm.split(":"))
  return h * 3600 + m * 60 + s

def solve():
  start = tm_to_int(input())
  class_start = tm_to_int(input())
  time, ratio = mii()
  
  time = time * (100 - ratio) // 100
  
  print(int(start + time <= class_start))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
