"""
[21030: Frequent Alphabet](https://www.acmicpc.net/problem/21030)

Tier: Silver 5 
Category: string
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
  a = inp()
  b = inp()

  d = {}

  for i in range(n):
    if a[i] == b[i]:
      d[a[i]] = d.get(a[i], 0) + 1
    else:
      d[a[i]] = d.get(a[i], 0) + 1
      d[b[i]] = d.get(b[i], 0) + 1
  
  print(max(d.values()))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()