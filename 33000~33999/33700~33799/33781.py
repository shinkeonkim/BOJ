"""
[33781: Diagnosis](https://www.acmicpc.net/problem/33781)

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

  D = mii()[1:]

  l = [mii()[1:] for _ in range(n)]
  
  s = set()

  for i in D:
    for j in l[i - 1]:
      s.add(j)
  
  print("yes" if len(s) == m else "no")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()