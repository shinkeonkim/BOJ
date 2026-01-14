"""
[7016: Recurring Decimals](https://www.acmicpc.net/problem/7016)

Tier: Silver 3 
Category: implementation, math, simulation, sorting
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
def near_integer(x): return int(x + 0.5) if x >= 0 else int(x - 0.5)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]
def transpose(matrix): return list(map(list, zip(*matrix)))

def sorting(k, sz):
  k = str(k)
  return sorted(list("0" * (sz - len(k)) + k))

def to_min(k, sz):
  return int("".join(sorting(k, sz)))

def to_max(k, sz):
  return int("".join(reversed(sorting(k, sz))))
  

def solve(a, sz):
  d = { str(a): 0 }
  i = 1
  
  while 1:
    mx = to_max(a, sz)
    mn = to_min(a, sz)
    
    ret = mx - mn
    key = str(ret)
    
    if d.get(key, -1) > -1:
      j = d[key]
      print(j, ret, i - j)
      return

    d[key] = i
    i += 1
    a = ret


if __name__ == "__main__":
  while 1:
    a, b = mii()
    
    if a == b == 0:
      break
    
    solve(a, b)
