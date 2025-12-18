"""
[32201: 눈사람](https://www.acmicpc.net/problem/32201)

Tier: Silver 3 
Category: data_structures, sorting, set, hash_set
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
  n = ii()
  
  first_ranks = mii()
  second_ranks = mii()

  first_ranks_dict = {v: i for i, v in enumerate(first_ranks)}
  second_ranks_dict = {v: i for i, v in enumerate(second_ranks)}
  
  max_up = -float('inf')
  
  for i in first_ranks:
    max_up = max(max_up, first_ranks_dict[i] - second_ranks_dict[i])
    
  for i in second_ranks:
    if max_up == first_ranks_dict[i] - second_ranks_dict[i]:
      print(i, end = " ")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
