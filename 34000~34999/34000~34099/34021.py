"""
[34021: [T] 스코어보드가 121분 남은 시점에서 프리즈되었습니다.](https://www.acmicpc.net/problem/34021)

Tier: Bronze 3 
Category: math, implementation, arithmetic
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
  N, M, L = mii()
  S = mii()

  mn = 2000
  for i in S:
    if i == -1:
      continue
    mn = min(mn, i)
  
  ans = 0
  if mn == 2000:
    ans = L
  else:
    ans = max(M - mn, L)
  
  if ans == 1:
    print("The scoreboard has been frozen with 1 minute remaining.")
  else:
    print(f"The scoreboard has been frozen with {ans} minutes remaining.")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()