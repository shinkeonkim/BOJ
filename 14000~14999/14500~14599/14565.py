"""
[14565: 역원(Inverse) 구하기](https://www.acmicpc.net/problem/14565)

Tier: Gold 2 
Category: extended_euclidean, math, modular_multiplicative_inverse, number_theory
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

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(a, mod):
  gcd, x, _ = extended_gcd(a, mod)

  if gcd != 1:
    return -1
  
  return x % mod


def solve():
  N, A = mii()

  print(N - A, mod_inverse(A, N))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()