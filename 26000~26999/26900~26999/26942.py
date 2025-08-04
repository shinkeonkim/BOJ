"""
[26942: Gruppindelning](https://www.acmicpc.net/problem/26942)

Tier: Silver 2 
Category: bfs, data_structures, dfs, disjoint_set, graphs, graph_traversal, hash_set, set
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
  l = [inp() for _ in range(n)]
  dd = {}

  for i in range(n):
    dd[l[i]] = i

  m = ii()
  group = [i for i in range(100001)]
  
  def find(a):
    if group[a] != a:
      group[a] = find(group[a])
    return group[a]

  def merge(a, b):
    a = find(a)
    b = find(b)

    if a == b:
      return

    group[b] = a

  for _ in range(m):
    a, b = isplit()
    merge(dd[a], dd[b])

  ans = set()

  for i in range(n):
    ans.add(find(i))

  print(len(ans))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
