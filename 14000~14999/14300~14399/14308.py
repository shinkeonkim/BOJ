"""
[14308: Safe Squares (Small)](https://www.acmicpc.net/problem/14308)

Tier: Silver 5
Category: implementation, bruteforcing
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
def arithmetic_seq_sum(a, n, d): return (a * n + n * (n - 1) * d  // 2)

def solve():
  R, C, K = mii()
  
  monsters = [mii() for _ in range(K)]
  
  mp = [[0] * (C + 1) for _ in range(R + 1)]
  
  for y, x in monsters:
    mp[y + 1][x + 1] = 1
  
  sm = [[0] * (C + 1) for _ in range(R + 1)]
  
  for i in range(1, R + 1):
    for j in range(1, C + 1):
      sm[i][j] = mp[i][j] + sm[i - 1][j] + sm[i][j - 1] - sm[i - 1][j - 1]
  
  ans = 0
  
  for y1 in range(1, R + 1):
    for x1 in range(1, C + 1):
      for y2 in range(y1, R + 1):
        for x2 in range(x1, C + 1):
          if (y1 - x1) != (y2 - x2):
            continue
          
          area = sm[y2][x2] - sm[y2][x1 - 1] - sm[y1 - 1][x2] + sm[y1 - 1][x1 - 1]
          
          if area == 0:
            # print(y1, x1, y2, x2)
            ans += 1
  
  return ans


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret}")