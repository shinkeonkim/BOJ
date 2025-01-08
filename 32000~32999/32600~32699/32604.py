"""
[32604: Jumbled Scoreboards](https://www.acmicpc.net/problem/32604)

Tier: Bronze 4 
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
  
  l = [mii() for _ in range(n)]
  
  for i in range(1, n):
    if l[i - 1][0] > l[i][0] or l[i-1][1] > l[i][1]:
      print("no")
      break
  else:
    print("yes")
  
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()