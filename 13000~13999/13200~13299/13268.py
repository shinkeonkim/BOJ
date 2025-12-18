"""
[13268: 셔틀런](https://www.acmicpc.net/problem/13268)

Tier: Silver 3 
Category: implementation, simulation, case_work
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


seg = [
  [0, 0],
  [1, 5],
  [6, 10],
  [11, 15],
  [16, 20],
]

def solve():
  k = int(input())
  
  target = [5, 0, 10, 0, 15, 0, 20, 0]
  target_idx = 0
  current = 0
  d = 1
  
  for _ in range(k):
    if current == target[target_idx]:
      target_idx = (target_idx + 1) % len(target)
      d *= -1
    
    current += d
    
  
  for i in range(len(seg)):
    if seg[i][0] <= current <= seg[i][1]:
      print(i)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
