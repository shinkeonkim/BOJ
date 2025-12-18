"""
[12186: Sort a scrambled itinerary (Small)](https://www.acmicpc.net/problem/12186)

Tier: Silver 3 
Category: graphs, data_structures, string, bruteforcing, graph_traversal, set, hash_set
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
def round_up_half(n): return floor(n + 0.5)


def solve():
  n = ii()

  l = []

  in_cnt = defaultdict(int)
  out_cnt = defaultdict(int)

  edge = {}

  for i in range(n):
    a = input()
    b = input()
    l.append((a, b))
    in_cnt[b] += 1
    in_cnt[a] += 0
    edge[a] = b
  
  start = None

  for k, v in in_cnt.items():
    if v == 0:
      start = k
      break

  ans = ""
  current = start
  while edge.get(current) is not None:
    ans += f"{current}-{edge[current]} "
    current = edge[current]

  return ans.strip()


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret}")
