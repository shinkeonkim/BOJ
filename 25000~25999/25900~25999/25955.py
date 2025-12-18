"""
[25955: APC는 쉬운 난이도 순일까, 아닐까?](https://www.acmicpc.net/problem/25955)

Tier: Silver 4 
Category: implementation, sorting
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

def f(x):
  tier = x[0]
  number = int(x[1:])
  k = "BSGPD".index(tier)
  
  return k * 1000 + (1000 - number)

def to_s(x):
  k = x // 1000
  number = 1000 - (x % 1000)
  return "BSGPD"[k] + str(number)

def solve():
  n = ii()
  l = [*map(f, input().split())]
  
  sorted_l = sorted(l)
  
  shuffled = []
  for i in range(n):
    if l[i] != sorted_l[i]:
      shuffled.append(i)
      
  if len(shuffled) == 0:
    print("OK")
  else:
    print("KO")

    print(*[to_s(sorted_l[i]) for i in shuffled])

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
