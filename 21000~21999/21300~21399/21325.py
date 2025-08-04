"""
[21325: Free food](https://www.acmicpc.net/problem/21325)

Tier: Silver 2 
Category: graphs, graph_traversal, dfs
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
  n, m = mii()
  parent = mii()
  people = mii()
  
  is_in = [False] * (n + 1)
  for p in people:
    is_in[p] = True
  
  children = defaultdict(list)

  root = -1
  for i in range(0, n):
    if parent[i] == 0:
      root = i + 1
    else:
      children[parent[i]].append(i + 1)
  
  ans = 0

  def dfs(node):
    nonlocal ans
    if is_in[node]:
      ans += 1
      return
    
    for child in children[node]:
      dfs(child)
  
  dfs(root)

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
