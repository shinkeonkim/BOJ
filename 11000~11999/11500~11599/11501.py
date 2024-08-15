"""
[11501: 주식](https://www.acmicpc.net/problem/11501)

Tier: Silver 2 
Category: greedy
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
  arr = mii()
  mx = 0
  ans = 0

  for i in range(n-1, -1, -1):
    if arr[i] > mx:
      mx = arr[i]
    else:
      ans += mx - arr[i]
  
  p(ans)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()