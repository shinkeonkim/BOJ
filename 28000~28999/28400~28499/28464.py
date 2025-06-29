"""
[28464: Potato](https://www.acmicpc.net/problem/28464)

Tier: Silver 5 
Category: greedy, sorting
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
  l = sorted(mii())

  i = 0
  j = n - 1

  big = 0
  small = 0
  while i < j:
    small += l[i]
    big += l[j]
    i += 1
    j -= 1
  
  if i == j:
    big += l[i]
  
  print(small, big)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()