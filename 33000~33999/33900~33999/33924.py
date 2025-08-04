"""
[33924: 신묘마루의 요술망치](https://www.acmicpc.net/problem/33924)

Tier: Bronze 1 
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


l = [[0] * 2 for _ in range(4)]

def cross_change(l, a, b):
  """X 자로 교차하여 교환하는 경우"""
  l[a][0], l[b][1] = l[b][1], l[a][0]
  l[a][1], l[b][0] = l[b][0], l[a][1]
  return l

def skill_a(l):
  return l[2:] + l[:2]

def skill_b(l):
  cross_change(l, 0, 1)
  cross_change(l, 2, 3)
  return l

def skill_c(l):
  cross_change(l, 0, 3)
  cross_change(l, 1, 2)
  return l

def skill_d(l):
  return [[l[1][0], l[0][0]], [l[2][0], l[0][1]], [l[3][0], l[1][1]], [l[3][1], l[2][1]]]

def solve():
  global l
  n, m = mii()
  l[n - 1][m - 1] = 1

  k = ii()
  s = inp()

  skills = {
      'A': skill_a,
      'B': skill_b,
      'C': skill_c,
      'D': skill_d
  }
  
  for action in s:
    l = skills[action](l)

  # 맛있는 햄버거가 있는 위치
  for i in range(4):
    for j in range(2):
      if l[i][j] == 1:
        p(i + 1, j + 1)
        return


solve()