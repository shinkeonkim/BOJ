"""
[33753: 주차 요금 정산하기](https://www.acmicpc.net/problem/33753)

Tier: Bronze 3 
Category: math
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
  A, B , C = mii()

  T = ii()

  if T <= 30:
    return A
  
  over_time = T - 30
  over_cnt = over_time // B + (over_time % B > 0)

  return A + C * over_cnt

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)