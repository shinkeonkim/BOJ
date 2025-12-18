"""
[31257: СИМЕТРИЧНА РЕДИЦА](https://www.acmicpc.net/problem/31257)

Tier: Bronze 1 
Category: bruteforcing, implementation, string
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


def is_palindrome(s: str) -> bool:
  return s == s[::-1]

def solve():
  n = ii()
  s = inp()

  if is_palindrome(s):
    p(0)
    return

  for i in range(1, n):
    crt = s[:i][::-1]
    k = s + crt

    if is_palindrome(k):
      p(i)
      p(crt)
      return


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
