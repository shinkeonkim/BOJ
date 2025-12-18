"""
[30786: 홀수 찾아 삼만리](https://www.acmicpc.net/problem/30786)

Tier: Silver 2 
Category: math, ad_hoc, parity
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
  n = int(inp())
  l = [mii() for _ in range(n)]
  
  chks = [] # 홀짝
  left = [] # 홀홀 또는 짝짝

  for i in range(n):
    if l[i][0] % 2 != l[i][1] % 2:
      chks.append(i + 1)
    else:
      left.append(i + 1)

  if len(left) == 0 or len(chks) == 0:
    print("NO")
    return
  
  print("YES")
  for i in chks + left:
    print(i, end =" ")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
