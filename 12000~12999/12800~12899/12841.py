"""
[12841: 정보대 등산](https://www.acmicpc.net/problem/12841)

Tier: Silver 2 
Category: prefix_sum
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
  n = ii()
  cross_dist = mii()
  left_dist = mii()
  right_dist = mii()


  left_prefix = [0] * (n)
  right_prefix = [0] * (n) # 뒤에서부터 누적하기
  
  for i in range(1, n):
    left_prefix[i] = left_prefix[i-1] + left_dist[i-1]
  
  for i in range(n - 2, -1, -1):
    right_prefix[i] = right_prefix[i+1] + right_dist[i]
  
  mn = float('inf')
  ans = n

  for i in range(n):
    dist = cross_dist[i] + left_prefix[i] + right_prefix[i]

    if dist < mn:
      mn = dist
      ans = i + 1
  
  print(ans, mn)
      
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
