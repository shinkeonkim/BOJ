"""
[28638: Результаты контеста](https://www.acmicpc.net/problem/28638)

Tier: Bronze 1 
Category: implementation
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


def to_i(s):
  h, m = map(int, s.split(':'))
  return h * 60 + m

def solve():
  n = int(input())
  records = [input().split() for _ in range(n)]
  for i in range(n):
    records[i][0] = to_i(records[i][0])
  
  is_solved = defaultdict(bool)
  fail_count = defaultdict(int)
  penalty = 0
  
  records.sort(key=lambda x: x[0])
  
  for time, problem, result in records:
    if result == 'CE':
      continue
    if result == 'OK':
      if not is_solved[problem]:
        is_solved[problem] = True
        penalty += time + fail_count[problem] * 20
    else:
      if not is_solved[problem]:
        fail_count[problem] += 1
  
  solved_cnt = sum(is_solved.values())
  print(solved_cnt, penalty)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
