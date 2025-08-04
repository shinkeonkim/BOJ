"""
[30082: Atvirutės](https://www.acmicpc.net/problem/30082)

Tier: Silver 2 
Category: bfs, dfs, graphs, graph_traversal
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
  N, M, K = map(int, input().split())

  linas_friends = [int(input()) for _ in range(M)]

  friend_graph = defaultdict(set)
  
  for _ in range(K):
    a, b = map(int, input().split())
    friend_graph[a].add(b)
    friend_graph[b].add(a)
  
  ans = 0

  queue = deque()
  visisted = [False] * (N + 1)

  for friend in linas_friends:
    queue.append(friend)

  while queue:
    current = queue.popleft()

    if visisted[current]:
      continue

    visisted[current] = True
    ans += 1

    for friend in friend_graph[current]:
      if not visisted[friend]:
        queue.append(friend)
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
