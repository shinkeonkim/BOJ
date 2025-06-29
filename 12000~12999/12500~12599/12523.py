"""
[12523: Twibet (Small)](https://www.acmicpc.net/problem/12523)

Tier: Silver 2 
Category: bfs, dfs, graphs, graph_traversal, implementation
"""


import sys
from collections import deque
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

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
  l = mii()

  adj = [[] for _ in range(n + 1)]

  for i in range(n):
    adj[l[i]].append(i + 1)
  


  for i in range(1, n + 1):
    visited = [False] * (n + 1)
    queue = deque([i])

    while queue:
      node = queue.popleft()
      if visited[node]:
        continue
      visited[node] = True

      for neighbor in adj[node]:
        if not visited[neighbor]:
          queue.append(neighbor)
    
    print(sum(visited))
  

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    print(f"Case #{t}:")
    ret = solve()
