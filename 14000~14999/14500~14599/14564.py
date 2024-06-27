"""
[14564: 두부 게임 (Tofu Game)](https://www.acmicpc.net/problem/14564)

Tier: Bronze 1 
Category: implementation, math, simulation
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
  n, m, crt = mii()
  
  center = m // 2 + 1
  
  while 1:
    a = ii()
    
    if a == center:
      p(0)
      break
    
    diff = a - center
    
    crt = (crt + diff - 1 + 10 * n) % n + 1
    
    p(crt)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()