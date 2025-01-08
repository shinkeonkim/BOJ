"""
[32306: Basketball Score](https://www.acmicpc.net/problem/32306)

Tier: Bronze 4 
Category: arithmetic, implementation, math
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
  a = mii()
  b = mii()
  
  A = a[0] + 2 * a[1] + 3 * a[2]
  B = b[0] + 2 * b[1] + 3 * b[2]
  
  if A > B:
    p(1)
  elif A < B:
    p(2)
  else:
    p(0)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()