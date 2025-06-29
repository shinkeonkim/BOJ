"""
[9322: 철벽 보안 알고리즘](https://www.acmicpc.net/problem/9322)

Tier: Silver 4 
Category: data_structures, string, set, hash_set
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
  first = isplit()
  second = isplit()

  quiz = isplit()

  d = defaultdict(list)

  for i in range(n):
    d[first[i]].append(i)
  for i in range(n):
    d[second[i]].append(i)
  
  d = d.values()

  d2 = {}

  for i in d:
    d2[i[0]] = i[1]
  
  for i in range(n):
    print(quiz[d2[i]], end=BLANK)
  print()


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()