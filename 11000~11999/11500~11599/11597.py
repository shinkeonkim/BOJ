"""
[11597: Excellence](https://www.acmicpc.net/problem/11597)

Tier: Silver 5 
Category: greedy, sorting
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

  l = [ii() for _ in range(n)]

  l.sort()

  mn = l[0] + l[-1]

  for i in range(1, n // 2 + 1):
    mn = min(mn, l[i] + l[-i - 1])
  p(mn)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()