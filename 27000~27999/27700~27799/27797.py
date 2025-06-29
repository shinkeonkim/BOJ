"""
[27797: Vestigium](https://www.acmicpc.net/problem/27797)

Tier: Bronze 1 
Category: arithmetic, implementation, math
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

  ans = [0, 0, 0]
  for i in range(n):
    ans[0] += l[i][i]

  for i in range(n):
    if n != len(set(l[i])):
      ans[1] += 1
  
  for i in range(n):
    if n != len(set([l[j][i] for j in range(n)])):
      ans[2] += 1
  
  return ans


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    p(f"Case #{t}: {ret[0]} {ret[1]} {ret[2]}")