"""
[32436: Enigma of the Jewelry Case](https://www.acmicpc.net/problem/32436)

Tier: Bronze 3 
Category: ad_hoc, implementation, simulation
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
  l = [mii() for _ in range(n)]
  
  a = True
  b = True
  
  for i in range(n - 1):
    if l[0][i] > l[0][i + 1]:
      a = False
  
  for i in range(n - 1):
    if l[i][0] > l[i + 1][0]:
      b = False
  
  if a and b:
    print(0)
  elif a:
    print(3)
  elif b:
    print(1)
  else:
    print(2)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()