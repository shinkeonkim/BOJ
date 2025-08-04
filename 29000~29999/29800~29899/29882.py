"""
[29882: Ranking](https://www.acmicpc.net/problem/29882)

Tier: Silver 3 
Category: data_structures, hash_set, sorting, set
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
  n = ii()
  l = [isplit() for _ in range(n)]

  d = defaultdict(lambda: 0)

  for name, problem, score in l:
    score = int(score)
    key = (name, problem)

    if d[key] < score:
      d[key] = score
  
  score_by_name = defaultdict(lambda: 0)
  for (name, problem), score in d.items():
    score_by_name[name] += score
  
  sorted_scores = sorted(score_by_name.items(), key=lambda x: (-x[1], x[0]))

  for k, v in sorted_scores:
    p(f"{k} {v}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
