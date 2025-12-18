"""
[24388: РАМКА](https://www.acmicpc.net/problem/24388)

Tier: Silver 5 
Category: arithmetic, case_work, math
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
  a, b, k = map(int, input().split())
  
  cnt = (a // k) * 2 + (b // k) * 2
  
  ar = []
  if a % k > 0:
    ar.append(a % k)
    ar.append(a % k)
  
  if b % k > 0:
    ar.append(b % k)
    ar.append(b % k)
  
  if len(ar) == 0:
    print(cnt)
    return
  
  ret = float('inf')
  if len(ar) == 2:
    for i in range(2):
      for j in range(2):
        groups = [0, 0]
        groups[i] += ar[0]
        groups[j] += ar[1]
        group_cnt = sum([1 for i in groups if i > 0])
            
        if all(group <= k for group in groups):
          ret = min(ret, group_cnt)
  
  if len(ar) == 4:
    for i in range(4):
      for j in range(4):
        for y in range(4):
          for x in range(4):
            groups = [0, 0, 0, 0]
            groups[i] += ar[0]
            groups[j] += ar[1]
            groups[y] += ar[2]
            groups[x] += ar[3]
            group_cnt = sum([1 for i in groups if i > 0])
            
            if all(group <= k for group in groups):
              ret = min(ret, group_cnt)
    
  print(cnt + ret)    

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
