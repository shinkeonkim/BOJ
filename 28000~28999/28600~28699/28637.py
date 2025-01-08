"""
[28637: Смена стиля](https://www.acmicpc.net/problem/28637)

Tier: Bronze 3 
Category: implementation, string
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
  s = inp()
  
  # CamalCase to sanke_case
  if s[0].isupper():
    p(s[0].lower(), end="")
  else:
    p(s[0], end="")
  
  for i in range(1, len(s)):
    if s[i].isupper():
      p("_", end="")
      p(s[i].lower(), end="")
    else:
      p(s[i], end="")
  p()


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
