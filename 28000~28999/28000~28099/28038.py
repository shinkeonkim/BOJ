"""
[28038: 2차원 좌표변환](https://www.acmicpc.net/problem/28038)

Tier: Silver 2 
Category: math, geometry
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor, cos, atan2
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


def orthogonal_to_polar_coordinate(x, y):
  r = sqrt(x**2 + y**2)
  theta = atan2(y, x)
  if theta < 0:
    theta += 2 * pi
  return r, theta


def polar_to_orthogonal_coordinate(r, theta):
  x = r * cos(theta)
  y = r * sin(theta)
  return x, y

def solve():
  case = int(input())
  a, b = mfi()
  if case == 1:
    k = orthogonal_to_polar_coordinate(a, b)
  else:
    k = polar_to_orthogonal_coordinate(a, b)
  print(f"{k[0]:.8f} {k[1]:.8f}")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
