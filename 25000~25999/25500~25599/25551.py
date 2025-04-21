"""
[25551: 멋쟁이 포닉스](https://www.acmicpc.net/problem/25551)

Tier: Bronze 1 
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
  A = mii()
  B = mii()
  C = mii()

  a = min(B[0], A[1], C[1])
  b = min(B[1], A[0], C[0])

  if a == b:
    print(a + b)
  elif a > b:
    print(2 * b + 1)
  else:
    print(2 * a + 1)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()