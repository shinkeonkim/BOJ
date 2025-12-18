"""
[9912: Lexical](https://www.acmicpc.net/problem/9912)

Tier: Silver 2 
Category: combinatorics, math
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
def round_up_half(n): return floor(n + 0.5)


def solve():
  n = ii()
  l = mii()

  left_numbers = set([i for i in range(n)])
  ans = 1

  for i in range(n):
    current = l[i]

    small_count = 0

    for j in left_numbers:
      if j < current:
        small_count += 1
    
    left_count = len(left_numbers)

    ans += small_count * factorial(left_count - 1)
  
    left_numbers.remove(current)
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
