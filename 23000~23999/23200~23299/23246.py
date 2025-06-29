"""
[23246: Sport Climbing Combined](https://www.acmicpc.net/problem/23246)

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
  l = [mii() for _ in range(n)]

  l.sort(key=lambda x : (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

  print(l[0][0], l[1][0], l[2][0])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()