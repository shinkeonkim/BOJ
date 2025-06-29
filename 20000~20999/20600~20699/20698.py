"""
[20698: Police Stations](https://www.acmicpc.net/problem/20698)

Tier: Silver 5 
Category: geometry, implementation, math
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

  x = []
  y = []

  for i in range(n):
    x.append(l[i][0])
    y.append(l[i][1])
  
  x.sort()
  y.sort()

  mid = [(x[0] + x[-1]) // 2, (y[0] + y[-1]) // 2]
  ans = [max(mid[0] - x[0], x[-1] - mid[0]), max(mid[1] - y[0], y[-1] - mid[1])]

  print(*ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()