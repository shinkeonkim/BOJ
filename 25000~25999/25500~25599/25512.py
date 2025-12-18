"""
[25512: 트리를 간단하게 색칠하는 최소 비용](https://www.acmicpc.net/problem/25512)

Tier: Silver 1 
Category: graphs, graph_traversal, bipartite_graph
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
SET_RECURSION = True
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

n = ii()
edges = [[] for _ in range(n)]
chk = [-1] * n
inv_cnt = {i: 0 for i in range(n)}
for _ in range(n - 1):
  a, b = mii()
  edges[a].append(b)
  inv_cnt[b] += 1

costs = [mii() for _ in range(n)]

def dfs(v, color):
  ret = 0
  chk[v] = color
  
  for nxt in edges[v]:
    ret += dfs(nxt, 1 - color)
  
  return ret + (costs[v][color])
    

def solve():
  root = [k for k, v in inv_cnt.items() if v == 0][0]
  print(min(dfs(root, 0), dfs(root, 1)))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
