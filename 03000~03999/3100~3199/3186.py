"""
[3186: 소변기](https://www.acmicpc.net/problem/3186)

Tier: Silver 3 
Category: implementation, string, simulation
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

COMPLETE = "COMPLETE"
USING = "USING"

def solve():
  K, L, N = mii()
  cnt = 0
  s = " " + inp()
  
  state = COMPLETE
  last_used_time = 0
  continuous_using_time = 0
  
  for t in range(1, N + 1):
    current = s[t]
    
    if current == '1':
      continuous_using_time += 1
      last_used_time = t
      
      if continuous_using_time >= K:
        state = USING
    else:
      continuous_using_time = 0
      if state == USING and t - last_used_time >= L:
        state = COMPLETE
        print(t)
        cnt += 1
  
  if state == USING:
    print(last_used_time + L)
    cnt += 1
  
  if cnt == 0:
    print("NIKAD")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
