"""
[6893: TopYodeller](https://www.acmicpc.net/problem/6893)

Tier: Bronze 1 
Category: implementation
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
  n, k = mii() # n명, k라운드

  total_score = defaultdict(lambda : 0)
  worsk_rank = defaultdict(lambda : 0)

  for _ in range(k):
    scores = mii()
  
    for i, score in enumerate(scores):
      total_score[i + 1] += score


    d = sorted(list(set(total_score.values())), reverse=True)
    d = {v: i + 1 for i, v in enumerate(d)}

    for k, v in total_score.items():
      worsk_rank[k] = max(worsk_rank[k], d[v])
    
  max_total_score = max(total_score.values())

  for i in range(1, n + 1):
    if total_score[i] == max_total_score:
      print(f"Yodeller {i} is the TopYodeller: score {total_score[i]}, worst rank {worsk_rank[i]}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
