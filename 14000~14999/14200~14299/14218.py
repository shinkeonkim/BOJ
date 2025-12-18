"""
[14218: 그래프 탐색 2](https://www.acmicpc.net/problem/14218)

Tier: Silver 1 
Category: graphs, graph_traversal, bfs, dfs
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

n = None
distances = []

def p_edge(l):
  for i in range(1, len(l)):
    print(-1 if l[i] == float('inf') else l[i], end=' ')
  print()

def bfs():
  q = deque([(1, 0)])
  
  while q:
    node, dist = q.popleft()
    
    if distances[node] <= dist:
      continue
    
    distances[node] = dist
    
    for nxt in edges[node]:
      if distances[nxt] > dist + 1:
        q.append((nxt, dist + 1))
  
  p_edge(distances)

def solve():
  global n, distances, edges
  n, m = mii()
  distances = [float('inf')] * (n + 1)
  
  l = [mii() for _ in range(m)]
  
  edges = defaultdict(list)
  for a, b in l:
    edges[a].append(b)
    edges[b].append(a)
  
  k = ii()
  
  adding = [mii() for _ in range(k)]
  
  for a, b in adding:
    distances = [float('inf')] * (n + 1)
    edges[a].append(b)
    edges[b].append(a)
    
    bfs()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
