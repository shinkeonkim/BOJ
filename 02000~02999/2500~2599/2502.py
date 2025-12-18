"""
[2502: 떡 먹는 호랑이](https://www.acmicpc.net/problem/2502)

Tier: Silver 1 
Category: math, dp, bruteforcing
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


def solve():
  D, K = mii() # D 일에 K개를 줬다.
  
  for prev_k in range(1, K):
    crt = K
    prev = prev_k
    l = [crt, prev]
    
    for _ in range(D - 2):
      crt, prev = prev, crt - prev
      l.append(prev)
    
    if all(i > 0 for i in l) and l[-1] <= l[-2]:
      print(l[-1])
      print(l[-2])
      break


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
