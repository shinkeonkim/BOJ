"""
[32643: 정민이의 수열 제조법](https://www.acmicpc.net/problem/32643)

Tier: Silver 1 
Category: math, number_theory, prefix_sum, primality_test, sieve
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
  N, M = mii()
  
  queries = [mii() for _ in range(M)]
  
  primes = [1] # 문제의 특수성으로 포함
  chk = defaultdict(lambda : True)

  chk[0] = chk[1] = False
  
  for i in range(2, N + 1):
    if chk[i]:
      primes.append(i)
      for j in range(i * i, N + 1, i):
        chk[j] = False
  
  for a, b in queries:
    print(bisect_right(primes, b) - bisect_left(primes, a))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
