"""
[9762: โรงงานลูกกวาด (Candy Factory)](https://www.acmicpc.net/problem/9762)

Tier: Silver 5 
Category: implementation, simulation, trees
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

d = {}

def f(i):
  ret = d.get(i, -1)

  if ret == -1:
    ret = min(f(2 * i), f(2 * i + 1))

    d[i] = d.get(i, 0) + ret
    d[2 * i] -= ret
    d[2 * i + 1] -= ret

  return ret

def solve():
  global d
  n = ii()
  l = mii()
  d = {}

  for i in range(n // 2 + 1, n + 1):
    d[i] = l[i - n // 2 - 1]
  
  f(1)

  # print(d)

  ans = 0

  for i in range(1, n + 1):
    ans += d[i]
  
  print(ans)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()