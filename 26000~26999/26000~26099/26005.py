"""
[26005: 나뭇잎 학회](https://www.acmicpc.net/problem/26005)

Tier: Silver 5 
Category: ad_hoc, arithmetic, math
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

  if n == 1:
    return 0
  
  if n == 2:
    return 2
  
  if n % 2 == 0:
    return n * n // 2
  
  return n * n // 2 + 1



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)