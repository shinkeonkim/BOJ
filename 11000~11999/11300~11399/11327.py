"""
[11327: Polynomial Boundaries](https://www.acmicpc.net/problem/11327)

Tier: Bronze 1 
Category: math, implementation
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


def solve():
  while 1:
    s = inp()

    if s == "0":
      break
    
    n, *l = map(int, s.split())
    x, y = mii()

    current = 1

    y_prime = 0

    for i in range(n):
      y_prime += l[i] * current
      current *= x
    
    if y_prime == y:
      print("On")
    elif y_prime < y:
      print("Outside")
    else:
      print("Inside")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()