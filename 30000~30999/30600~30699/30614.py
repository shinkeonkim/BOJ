"""
[30614: Port Robot](https://www.acmicpc.net/problem/30614)

Tier: Bronze 1 
Category: implementation, data_structures, stack
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

stack = []

def push(x):
  stack.append(x)

def pop():
  if stack:
    return stack.pop()
  return -1

def solve():
  n = ii()
  s = inp()

  for current in s:
    if current.isupper():
      ret = pop()

      if ret == -1 or ret != current.lower():
        return 0
    else:
      push(current)

  return 0 if stack else 1

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

    print(ret)
