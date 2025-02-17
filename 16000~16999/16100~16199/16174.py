"""
[16173: 점프왕 쩰리 (Small)](https://www.acmicpc.net/problem/16173)

Tier: Silver 4 
Category: bfs, bruteforcing, dfs, graphs, graph_traversal, implementation
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
  l = [mii() for _ in range(n)]

  D = [[-1] * n for _ in range(n)]
  
  Q = [[0, 0]]

  while Q:
    y, x  = Q.pop(0)

    if D[y][x] == 0:
      continue

    D[y][x] = 0 

    if y + l[y][x] < n:
      Q.append([y + l[y][x], x])
    
    if x + l[y][x] < n:
      Q.append([y, x + l[y][x]])
  
  return "HaruHaru" if D[n-1][n-1] == 0 else "Hing"


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)
