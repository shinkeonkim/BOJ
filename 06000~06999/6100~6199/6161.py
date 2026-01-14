"""
[6161: iCow](https://www.acmicpc.net/problem/6161)

Tier: Silver 5 
Category: implementation, simulation
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

def solve():
  N, T = mii()
  scores = [ii() for _ in range(N)]
  ans = []
  
  for t in range(T):
    mx = max(scores)
    mx_idx = scores.index(mx)
    ans.append(mx_idx + 1)
    
    distributing_score = mx // (N - 1)
    extra_score = mx % (N - 1)
    
    scores[mx_idx] = 0
    
    for i in range(N):
      if i == mx_idx:
        continue
      
      scores[i] += distributing_score
      if extra_score > 0:
        scores[i] += 1
        extra_score -= 1
  print(*ans, sep="\n")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
