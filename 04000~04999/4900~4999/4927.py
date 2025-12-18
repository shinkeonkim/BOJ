"""
[4927: Casting Out Nines](https://www.acmicpc.net/problem/4927)

Tier: Bronze 1 
Category: math, implementation, string, arithmetic, parsing
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

def digit_sum(n):
  return sum(int(d) for d in str(n))

def solve(s):
  a,r = s.split("=")
  r = int(r)
  
  if '+' in a:
    x, y = a.split('+')
    x, y = int(x), int(y)

    if digit_sum(r) % 9 == (digit_sum(x) + digit_sum(y)) % 9:
      return True

    return False
  else:
    x, y = a.split('*')
    x, y = int(x), int(y)

    if digit_sum(r) % 9 == (digit_sum(x) * digit_sum(y)) % 9:
      return True
    return False


if __name__ == "__main__":
  t = 0
  while 1:
    t += 1
    s = input()

    if s == '.':
      break

    ret = solve(s[:-1])

    print(f"{t}. {'PASS' if ret else 'NOT!'}")
