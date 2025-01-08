"""
[32685: 4-LSB](https://www.acmicpc.net/problem/32685)

Tier: Bronze 2 
Category: bitmask, implementation, math
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

def f():
  s = bin(ii())[2:][-4:]
  
  return "0" * (4 - len(s)) + s

def solve():
  a = f()
  b = f()
  c = f()

  s = a + b + c

  ans = str(int(s, 2))

  ans = "0" * (4 - len(ans)) + ans

  p(ans)




if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()