"""
[32860: 수수수수퍼노바](https://www.acmicpc.net/problem/32860)

Tier: Bronze 2 
Category: arithmetic, implementation, math
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
  y, idx = mii()
  idx -=1

  s = ""
  if idx < 26:
    s = chr(idx+65)
  else:
    while idx >= 26:
      s += chr(idx%26+97)
      idx = idx//26 - 1
    s += chr(idx+97)
    s = s[::-1]
  print(f"SN {y}{s}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()