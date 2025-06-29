"""
[6426: Psuedo-Random Numbers](https://www.acmicpc.net/problem/6426)

Tier: Bronze 1 
Category: arithmetic, implementation, math, simulation
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
  tc = 1
  while 1:
    Z, I, M, L = mii()

    if Z == I == M == L == 0:
      break

    d = {}
    cnt = 0

    while d.get(L, None) == None:
      d[L] = cnt

      L = (Z * L + I) % M 
      cnt += 1
    
    p("Case {}: {}".format(tc, cnt - d[L]))
    tc += 1


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()