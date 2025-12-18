"""
[5600: 품질검사](https://www.acmicpc.net/problem/5600)

Tier: Silver 2 
Category: ad_hoc, implementation
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
  a, b, c = mii()
  n = ii()
  
  results = [mii() for _ in range(n)]
  
  stats = [2] * (a + b + c)
  
  fail_results = []
  
  for i in results:
    if i[-1] == 1:
      for j in i[:-1]:
        stats[j - 1] = 1
    else:
      fail_results.append((i[0] - 1, i[1] -1 , i[2] - 1))
      
  
  while 1:
    is_changed = False
    
    k = []
    for i in range(len(fail_results)):
      tmp = []
      for j in fail_results[i]:
        if stats[j] == 1:
          is_changed = True
          continue
        tmp.append(j)
      k.append(tmp)
    
    if not is_changed:
      break
    
    for i in k:
      if len(i) == 1:
        stats[i[0]] = 0
    
    fail_results = k

  print(*stats, sep="\n")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
