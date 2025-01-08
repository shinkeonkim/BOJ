"""
[32801: Generalized FizzBuzz](https://www.acmicpc.net/problem/32801)

Tier: Bronze 4 
Category: bruteforcing, implementation, math, number_theory
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
  n, a, b = mii()

  l = [0, 0, 0]

  for i in range(1, n+1):
    if i % a == 0 and i % b == 0:
      l[2] += 1
    elif i % a == 0:
      l[0] += 1
    elif i % b == 0:
      l[1] += 1
  
  p(*l)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()