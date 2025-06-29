"""
[33964: 레퓨닛의 덧셈](https://www.acmicpc.net/problem/33964)

Tier: Bronze 4 
Category: math, arithmetic
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
  X, Y = mii()
  X, Y = min(X, Y), max(X, Y)

  s = "2" * X + "1" * (Y - X)
  print(s[::-1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()