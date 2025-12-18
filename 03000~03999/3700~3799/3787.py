"""
[3787: Count on Canton](https://www.acmicpc.net/problem/3787)

Tier: Silver 5 
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
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  while 1:
    try:
      n = int(input())
    except:
      break
  
    crt = 1
    s = 0

    while s + crt + 1 <= n:
      s += crt
      crt += 1
    
    need = crt + 1
    k = n - s
    
    if crt % 2:
      a, b = need - k, k
    else:
      a, b = k, need - k

    print(f"TERM {n} IS {a}/{b}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
