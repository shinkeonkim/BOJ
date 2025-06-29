"""
[32185: 꿈 열정 나눔](https://www.acmicpc.net/problem/32185)

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
  n, m = mii()

  k, *l = [[sum(mii()), i] for i in range(n + 1)]
  k = k[0]

  l.sort(key=lambda x: x[0], reverse=True)


  z = 1
  print(0, end=BLANK)
  for i in range(n):
    if z == m:
      break
    if l[i][0] <= k:
      z += 1
      print(l[i][1], end=BLANK)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()