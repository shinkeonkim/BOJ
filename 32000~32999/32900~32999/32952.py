"""
[32952: 비트코인 반감기](https://www.acmicpc.net/problem/32952)

Tier: Bronze 2 
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
  R, K, M = mii()

  r = R
  r_step = 0

  while r > 0:
    r = r // 2
    r_step += 1

  m_step = M // K

  ret = R

  if r_step > m_step:
    return R // (2 ** m_step)
  else:
    return 0
  
  # return ret // (2 ** m_step)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)