"""
[34750: 추석은 언제나 좋아](https://www.acmicpc.net/problem/34750)

Tier: Bronze 4 
Category: math, implementation, arithmetic
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
# 받은 금액이 
# $1\,000\,000$원 이상일 경우: 금액의 
# $20\%$ 
# 받은 금액이 
# $500\,000$원 이상 
# $1\,000\,000$원 미만일 경우: 금액의 
# $15\%$ 
# 받은 금액이 
# $100\,000$원 이상 
# $500\,000$원 미만일 경우: 금액의 
# $10\%$ 
# 받은 금액이 
# $100\,000$원 미만일 경우: 금액의 
# $5\%$ 

def solve():
  n = ii()
  
  if n >= 1_000_000:
    k = n // 5
    print(k, n - k)
  elif n >= 500_000:
    k = n * 15 // 100
    print(k, n - k)
  elif n >= 100_000:
    k = n // 10
    print(k, n - k)
  else:
    k = n // 20
    print(k, n - k)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
