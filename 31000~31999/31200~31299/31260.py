"""
[31260: ПРАВОЪГЪЛНИК](https://www.acmicpc.net/problem/31260)

Tier: Bronze 2 
Category: arithmetic, geometry, math
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
  x, y = mii()
  d = ii()
  
  # x * 100 + y == 2 * (a + b) 
  
  # a + d = b
  
  # 2 * (a + a + d) = x * 100 + y
  
  
  # (2 * a + d) = (x * 100 + y) // 2
  
  a = ((x * 100 + y) // 2 - d) // 2
  
  b = a + d
  
  print(b // 100, b % 100)
  print(a // 100, a % 100)
  
  
  
  
  
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()