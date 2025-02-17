"""
[33213: Fermatovi Fakini](https://www.acmicpc.net/problem/33213)

Tier: Bronze 3 
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
  n = ii()
  l = mii()

  odd = []
  even = []

  for i in l:
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)

  start = -1
  z = []
  if len(odd) < len(even):
    z = even
    start = 2
  else:
    z = odd
    start = 1
  

  z.sort()
  for i in z:
    if i == start:
      start += 2
    else:
      return start
  return start
    



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    print(ret)