"""
[26559: Friends](https://www.acmicpc.net/problem/26559)

Tier: Silver 5 
Category: sorting
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
  l = [isplit() for _ in range(n)]

  l.sort(key=lambda x: -int(x[1]))

  l = [i[0] for i in l]
  print(*l, sep=", ")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()