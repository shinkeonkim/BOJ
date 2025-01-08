"""
[32171: 울타리 공사](https://www.acmicpc.net/problem/32171)

Tier: Bronze 2 
Category: arithmetic, geometry, implementation, math
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


def f(l):
  return ((l[2] - l[0]) + (l[3] - l[1])) * 2

def solve():
  n = ii()
  
  prev = mii() 
  
  print(f(prev))
  
  for _ in range(n - 1):
    here = mii()
    
    prev[0] = min(prev[0], here[0])
    prev[1] = min(prev[1], here[1])
    prev[2] = max(prev[2], here[2])
    prev[3] = max(prev[3], here[3])
    
    print(f(prev))
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()