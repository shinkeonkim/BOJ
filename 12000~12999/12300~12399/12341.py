"""
[12341: Fair and Square (Large2)](https://www.acmicpc.net/problem/12341)

Tier: Platinum 3
Category: arbitrary_precision, backtracking, math, precomputation
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
def near_integer(x): return int(x + 0.5) if x >= 0 else int(x - 0.5)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]
def transpose(matrix): return list(map(list, zip(*matrix)))
def arithmetic_seq_sum(a, n, d): return (a * n + n * (n - 1) * d  // 2)

MAX = 10 ** 15
d = [1, 2, 3]

cases = {
  0: [],
  1: ["0", "1"]
}

def get_cases(left_digits):
  if cases.get(left_digits, False):
    return cases[left_digits]

  ret = []
  sub = get_cases(left_digits - 1)
  
  for i in sub:
    ret.append("1" + i)
    ret.append("0" + i)
  
  cases[left_digits] = ret
  return cases[left_digits]

def init():
  
  print(len(get_cases(5)))

  for digits_count in (1, 26):
    # digis_count 만큼 + 1 또는 0  + digits_count 만큼
    # digis_count 만큼 + digits_count 만큼 
    left_digits = digits_count - 1
    cases = get_cases(left_digits)
      
  
  

def solve():
  a, b = mii()


if __name__ == "__main__":
  tc = ii()
  init()
  print(d)
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret}")