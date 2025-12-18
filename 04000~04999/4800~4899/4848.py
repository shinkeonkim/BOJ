"""
[4848: 집합 숫자 표기법](https://www.acmicpc.net/problem/4848)

Tier: Silver 2 
Category: data_structures, hash_set, string, set
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


def to_num(s):
  stk = 0
  ret = 0
  for i in s:
    if i =='{':
      stk += 1
    elif i == '}':
      stk -= 1
    ret = max(ret, stk)
  return ret - 1


def to_s(n):
  if n == 0:
    return '{}'
  
  ret = '{'
  for i in range(n):
    ret += to_s(i)
    if i != n - 1:
      ret += ','
  ret += '}'

  return ret


def solve():
  print(to_s(to_num(input()) + to_num(input())))


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
