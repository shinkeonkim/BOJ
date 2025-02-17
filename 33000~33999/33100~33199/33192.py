"""
[33192: Divar’s Salaries](https://www.acmicpc.net/problem/33192)

Tier: Bronze 3 
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
  x, k, h = mii()
  k -= h

  A = min(k, 140)
  B = max(0, k - 140)

  # print(A, B, A * x + B * x * 3 // 2, h * x * 2)

  money = A * x + B * x * 3 // 2 + h * x * 2
  print(format(money, ',d'))


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()