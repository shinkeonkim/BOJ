"""
[28081: 직사각형 피자](https://www.acmicpc.net/problem/28081)

Tier: Silver 1 
Category: sorting, binary_search, two_pointer
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
  W, H, K = mii()
  
  N = ii()
  y_cuts = mii() # 가로 커트
  
  M = ii()
  x_cuts = mii() # 세로 커트
  
  y_cuts = [0] + y_cuts + [H]
  x_cuts = [0] + x_cuts + [W]

  widths = [y_cuts[i] - y_cuts[i-1] for i in range(1, len(y_cuts))]
  heights = [x_cuts[i] - x_cuts[i-1] for i in range(1, len(x_cuts))]
  
  cnt = 0
  
  widths.sort()
  heights.sort()
  
  for w in widths:
    maximum_height = K // w
    cnt += bisect_right(heights, maximum_height)
  
  print(cnt)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
