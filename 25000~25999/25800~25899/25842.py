"""
[25842: Tetrooj Box](https://www.acmicpc.net/problem/25842)

Tier: Silver 5 
Category: implementation, simulation
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
  n, m = mii()

  l = [0 for _ in range(n + 1)]

  for _ in range(m):
    w, h, x = mii()

    mx = 0

    for i in range(x, x + w):
      mx = max(mx, l[i])
    
    for i in range(x, x + w):
      l[i] = mx + h
  
  print(max(l))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()