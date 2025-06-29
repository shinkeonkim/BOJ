"""
[32403: 전구 주기 맞추기](https://www.acmicpc.net/problem/32403)

Tier: Silver 5 
Category: bruteforcing, math, number_theory
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "
INF = 10**9

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
  n, t = mii()
  l = mii()
  ans = 0

  ar = []

  for i in range(1, t+1):
    if t % i == 0:
      ar.append(i)

  for i in range(n):
    current = l[i]
    mn = INF

    if t % current == 0:
      continue

    for j in ar:
      mn = min(mn, abs(j - current))
  
    ans += mn
  
  p(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()