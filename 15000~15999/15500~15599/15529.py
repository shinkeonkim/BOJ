"""
[15529: Best Matched Pair](https://www.acmicpc.net/problem/15529)

Tier: Bronze 1 
Category: bruteforcing
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


def f(n):
  k = str(n)
  crt = int(k[0])

  for i in k[1:]:
    if int(i) != crt + 1:
      return False
    crt = int(i)
  return True

def solve():
  n = ii()
  l = mii()
  mx = -1

  for i in range(n):
    for j in range(i+1, n):
      c = l[i] * l[j]

      if f(c):
        mx = max(mx, c)
  p(mx)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
