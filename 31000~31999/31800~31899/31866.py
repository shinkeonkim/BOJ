"""
[31866: 손가락 게임](https://www.acmicpc.net/problem/31866)

Tier: Bronze 2 
Category: case_work, implementation
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


def f(cnt):
  # 바위, 가위, 보
  d = {0: 0, 2: 1, 5: 2}
  
  return d.get(cnt, -1)


def solve():
  a, b = map(f, mii())
  
  if a == b:
    return "="  

  if a == -1:
    return "<"

  if b == -1:
    return ">"

  if (a + 1) % 3 == b:
    return ">"

  return "<"


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)
