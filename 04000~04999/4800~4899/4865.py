"""
[4865: Shortest Prefixes](https://www.acmicpc.net/problem/4865)

Tier: Silver 4 
Category: string, bruteforcing
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

SYS_INPUT = False
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
  count = Counter()
  l = []

  while 1:
    try:
      s = input()
    except EOFError:
      break

    l.append(s)
  
  for s in l:
    for i in range(1, len(s) + 1):
      count[s[:i]] += 1
  
  for s in l:
    for j in range(1, len(s) + 1):
      if count[s[:j]] == 1:
        print(s, s[:j])
        break
    else:
      print(s, s)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
