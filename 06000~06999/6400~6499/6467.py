"""
[6467: Prime Cuts](https://www.acmicpc.net/problem/6467)

Tier: Silver 5 
Category: math, implementation, number_theory, primality_test
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
  is_prime = [True] * (1001)
  primes = [1]

  for i in range(2, 1001):
    if is_prime[i]:
      primes.append(i)
      for j in range(i * i, 1001, i):
        is_prime[j] = False
  
  while 1:
    try:
      N, C = mii()
    except:
      break
    
    n_primes = primes[:bisect_right(primes, N)]
    
    ln = len(n_primes)
    
    print(N, C, end=": ")
    
    if ln % 2 == 0:
      start = ln // 2 - C
      end = ln // 2 + C
      print(*n_primes[max(0, start):min(ln, end)])
    else:
      start = ln // 2 - C + 1
      end = ln // 2 + C
      print(*n_primes[max(0, start):min(ln, end)])

    print()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
