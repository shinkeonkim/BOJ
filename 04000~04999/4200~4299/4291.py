"""
[4291: Brownie Points I](https://www.acmicpc.net/problem/4291)

Tier: Bronze 1 
Category: implementation, simulation
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
  while 1:
    n = ii()
    
    if n == 0:
      break

    l = [mii() for _ in range(n)]
    
    center = l[n // 2]
    A = B = 0

    for x, y in l:
      x -= center[0]
      y -= center[1]
      
      if x == 0 or y == 0:
        continue
    
      if (x > 0) == (y > 0):
        A += 1
      else:
        B += 1
    
    p(A, B)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()