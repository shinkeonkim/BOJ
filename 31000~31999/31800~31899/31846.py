"""
[31846: 문자열 접기](https://www.acmicpc.net/problem/31846)

Tier: Silver 4 
Category: implementation, bruteforcing
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


def f(s):
  ret = 0
  for i in range(1, len(s)):
    a = s[:i][::-1]
    b = s[i:]

    k = 0
    for j in range(min(len(a), len(b))):
      if a[j] == b[j]:
        k += 1
    ret = max(ret, k)
  
  return ret
    

def solve():
  n = ii()
  s = inp()

  q = ii()

  queries = [mii() for _ in range(q)]

  for l, r in queries:
    sub_s = s[l-1:r]

    print(f(sub_s))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
