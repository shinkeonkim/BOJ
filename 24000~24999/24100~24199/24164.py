"""
[24164: 光ファイバー網の整備 (Fiber)](https://www.acmicpc.net/problem/24164)

Tier: Silver 1 
Category: bfs, data_structures, dfs, disjoint_set, graphs, graph_traversal
"""


import sys
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
  m = ii()

  adj = [[] for _ in range(n + 1)]
  l = [mii() for _ in range(m)]

  for a, b in l:
    adj[a].append(b)
    adj[b].append(a)

  chk = [0] * (n + 1)

  cnt = 0

  for i in range(1, n + 1):
    if chk[i]:
      continue
    
    cnt += 1

    from collections import deque
    q = deque([i])

    while q:
      here = q.popleft()
      chk[here] = 1

      for nxt in adj[here]:
        if chk[nxt]:
          continue

        chk[nxt] = 1
        q.append(nxt)
  
  print(cnt - 1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()