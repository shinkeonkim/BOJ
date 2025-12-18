"""
[4881: 자리수의 제곱](https://www.acmicpc.net/problem/4881)

Tier: Silver 3 
Category: bruteforcing, data_structures, hash_set, implementation, set
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

def f(k):
  ret = 0
  while k > 0:
    ret += (k % 10) ** 2
    k //= 10
  
  return ret
  

def solve(a, b):
  a_d = defaultdict(lambda: -1)
  b_d = defaultdict(lambda: -1)
  
  current = a
  cnt = 1
  while 1:
    if a_d[current] != -1:
      break
    a_d[current] = cnt
    cnt += 1
    
    current = f(current)
  
  current = b
  cnt = 1
  while 1:
    if b_d[current] != -1:
      break
    b_d[current] = cnt
    cnt += 1
    
    current = f(current)
  
  ans = float('inf')
  for k, v in a_d.items():
    if b_d[k] == -1:
      continue
      
    ans = min(ans, v + b_d[k])
  
  print(a, b, ans if ans != float('inf') else 0)


if __name__ == "__main__":
  while 1:
    a, b = map(int, input().split())
    if a == b == 0:
      break
    
    solve(a, b)