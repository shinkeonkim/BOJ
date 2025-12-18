"""
[33886: 카드 뭉치](https://www.acmicpc.net/problem/33886)

Tier: Silver 2 
Category: dp
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
SET_RECURSION = True
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


n = ii()
l = mii()

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]


def f(start, end):
  if start > end:
    return 0
  
  if dp[start][end] != float('inf'):
    return dp[start][end]

  if start == end:
    dp[start][end] = 1
    return 1
  
  # print(start, end)

  dp[start][end] = float('inf')

  target = l[start] # 해당 카드보다 더 큰 갯수가 있을 수 없다.
  
  for i in range(start, min(end + 1, start + target)):
    dp[start][end] = min(dp[start][end], 1 + f(i + 1, end))

  return dp[start][end]

print(f(0, n - 1))