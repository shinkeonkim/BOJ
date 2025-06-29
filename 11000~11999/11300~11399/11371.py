"""
[11371: The Big Eye in the Sky](https://www.acmicpc.net/problem/11371)

Tier: Silver 4 
Category: geometry, math
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor, atan2
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
  arctan2 = lambda x, y: (180 / pi) * atan2(x, y)

  while True:
    a, b = mii()

    if a == b == 0:
      break
    
    print(round(arctan2(b, a)))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()