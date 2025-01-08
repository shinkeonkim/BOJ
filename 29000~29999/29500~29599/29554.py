"""
[29554: Ситха джедай против](https://www.acmicpc.net/problem/29554)

Tier: Bronze 2 
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
  n = ii()
  A = mii()
  a_diff = mii()

  B = mii()
  b_diff = mii()

  for _ in range(0, 10000):
    chk = True

    for i in range(n):
      if A[i] < B[i]:
        chk = False
        break
    
    for i in range(n):
      A[i] += a_diff[i]
      B[i] += b_diff[i]
    
    if chk:
      print(_)
      return
  
  print("Strong is dark side of the force.")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()