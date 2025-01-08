"""
[4903: Relax! It’s just a game](https://www.acmicpc.net/problem/4903)

Tier: Bronze 1 
Category: combinatorics, math
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
  while 1:
    a, b = mii()
    
    if a == b == -1:
      break
    
    possibilities = factorial(a + b) // (factorial(a) * factorial(b))
    
    if a + b == possibilities:
      print(f"{a}+{b}={a + b}")
    else:
      print(f"{a}+{b}!={a + b}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()