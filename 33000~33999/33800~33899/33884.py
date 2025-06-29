"""
[33884: 클리크 조절](https://www.acmicpc.net/problem/33884)

Tier: Bronze 1 
Category: ad_hoc, geometry
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
  l = sorted([mii() for _ in range(n)])
  l2 = sorted([mii() for _ in range(n)])

  print(l2[0][0] - l[0][0], l2[0][1] - l[0][1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()