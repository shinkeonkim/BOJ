"""
[26258: 다중 일차 함수](https://www.acmicpc.net/problem/26258)

Tier: Silver 3 
Category: binary_search, math
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


n = int(inp())
  
l = [mii() for _ in range(n)]
  

def less_mx_idx(k: float):
  left = 0 
  right = n - 1
  ans = -1
  
  while left <= right:
    mid = (left + right) // 2
    
    if l[mid][0] < k:
      ans = max(ans, mid)
      left = mid + 1
    else:
      right = mid - 1
  
  return ans

def greater_mn_idx(k: float):
  left = 0 
  right = n - 1
  ans = n
  
  while left <= right:
    mid = (left + right) // 2
    
    if l[mid][0] > k:
      ans = min(ans, mid)
      right = mid - 1
    else:
      left = mid + 1
  
  return ans

Q = ii()

for _ in range(Q):
  k = float(inp())
  
  a = less_mx_idx(k)
  b = greater_mn_idx(k)
  
  if a == -1 or b == n or l[a][1] == l[b][1]:
    print(0)
  elif l[a][1] < l[b][1]:
    print(1)
  else:
    print(-1)
