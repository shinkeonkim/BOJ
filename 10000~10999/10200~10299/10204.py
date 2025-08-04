"""
[10204: Neighborhoods in Graphs](https://www.acmicpc.net/problem/10204)

Tier: Silver 2 
Category: bfs, dfs, floyd_warshall, graphs, graph_traversal, parsing, shortest_path, string
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

INF = float("inf")

def solve():
  n, e, *l, s = isplit()
  n = int(n)
  e = int(e)
  s = int(s[1:])

  adj = defaultdict(list)

  for i in range(0, len(l), 2):
    a = int(l[i][1:])
    b = int(l[i+1][1:])
    adj[a].append(b)
    adj[b].append(a)
  
  dist = [INF] * (n + 1)

  q = deque([(s, 0)])

  while q:
    node, dis = q.popleft()

    if dist[node] <= dis:
      continue

    dist[node] = dis

    for nei in adj[node]:
      if dist[nei] > dis + 1:
        q.append((nei, dis + 1))
    
  ans = 0

  for i in range(1, n + 1):
    if i == s:
      continue
    if dist[i] <= 2:
      ans += 1
  
  print(f"The number of supervillains in 2-hop neighborhood of v{s} is {ans}")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
