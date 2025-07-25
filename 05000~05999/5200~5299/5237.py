"""
[5237: Connected or Not Connected](https://www.acmicpc.net/problem/5237)

Tier: Silver 3 
Category: bfs, dfs, graphs, graph_traversal
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter

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
  n, k, *l = mii()

  edges = defaultdict(list)
  for i in range(0, len(l), 2):
    a, b = l[i], l[i+1]
    edges[a].append(b)
    edges[b].append(a)
  
  visited = [False] * (n)

  def dfs(node):
    if visited[node]:
      return
    visited[node] = True
    for neighbor in edges[node]:
      dfs(neighbor)

  dfs(0)

  if all(visited):
    p("Connected.")
  else:
    p("Not connected.")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()