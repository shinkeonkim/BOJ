"""
[32841: Welcome Sign](https://www.acmicpc.net/problem/32841)

Tier: Bronze 2 
Category: implementation
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
  l = [inp() for _ in range(n)]

  cnt = 1

  for i in range(n):
    space = m - len(l[i])

    if space % 2 == 0:
      left = space // 2
      right = space // 2
    else:
      left = space // 2
      right = space // 2

      if cnt % 2 == 0:
        left += 1
      else:
        right += 1
      cnt += 1

    
    print("."*left + l[i] + "."*right)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()