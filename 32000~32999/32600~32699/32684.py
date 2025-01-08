"""
[32684: 장기](https://www.acmicpc.net/problem/32684)

Tier: Bronze 4 
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
  weight_a = [13, 7, 5, 3, 3, 2]
  weight_b = [13, 7, 5, 3, 3, 2]
  a = mii()
  b = mii()

  A = [a[i] * weight_a[i] for i in range(6)]
  B = [b[i] * weight_b[i] for i in range(6)]

  A = sum(A)
  B = sum(B) + 1.5

  if A > B:
    print("cocjr0208")
  else:
    print("ekwoo")
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()