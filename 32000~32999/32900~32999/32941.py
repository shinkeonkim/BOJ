"""
[32941: 왜 맘대로 예약하냐고](https://www.acmicpc.net/problem/32941)

Tier: Bronze 4 
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
  T, X = mii()

  N = ii()

  l = []
  ret = True

  for _ in range(N):
    inp()

    z = mii()

    if X in z:
      continue
    else:
      ret = False


  if ret:
    print("YES")
  else:
    print("NO")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()