"""
[12340: Fair and Square (Large1)](https://www.acmicpc.net/problem/12340)

Tier: Silver 1
Category: math, string, precomputation
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


MAX = 10 ** 14
d = [0, ]

def is_palindrome(s):
  s = str(s)
  return s == s[::-1]


def init():
  i = 1
  cnt = 0
  
  while i * i <= MAX:
    if is_palindrome(i) and is_palindrome(i * i):
      cnt += 1
    d.append(cnt)
    i += 1

def solve():
  a, b = mii()
  
  a_sq = int(sqrt(a))
  
  if a_sq * a_sq < a:
    a_sq += 1 # a_sq - 1 구간을 뺄 예정
  
  b_sq = int(sqrt(b))
  
  # print(a_sq, b_sq, d[:10])
  return d[b_sq] - d[a_sq - 1]


if __name__ == "__main__":
  tc = ii()
  init()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret}")