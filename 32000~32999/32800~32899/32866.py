"""
[32866: 코인의 신 건모](https://www.acmicpc.net/problem/32866)

Tier: Bronze 3 
Category: arithmetic, math
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
  org = ii()
  x = ii()

  current = org * (100 - x) / 100
  print(org / current * 100 - 100)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
