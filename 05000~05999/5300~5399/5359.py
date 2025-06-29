"""
[5359: Music](https://www.acmicpc.net/problem/5359)

Tier: Bronze 1 
Category: bruteforcing, implementation
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
  n, m, c = mii()
  l = mii()
  cnt = 0

  for i in range(0, n - m + 1):
    sub = l[i:i+m]

    mx = max(sub)
    mn = min(sub)

    if mx - mn <= c:
      cnt += 1

  p(cnt)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()