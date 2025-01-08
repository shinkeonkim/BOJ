"""
[32369: 양파 실험](https://www.acmicpc.net/problem/32369)

Tier: Bronze 4 
Category: implementation, simulation
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
  n, A, B = mii()
  
  a = b = 1
  for _ in range(n):
    a += A
    b += B
    
    if a < b:
      a, b = b, a
    elif a == b:
      b -= 1
  
  print(a, b)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()