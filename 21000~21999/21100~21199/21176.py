"""
[21176: Smoothie Stand](https://www.acmicpc.net/problem/21176)

Tier: Bronze 1 
Category: arithmetic, bruteforcing, implementation, math
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
  k, r = mii()
  
  cap = mii()
  
  mx = 0
  
  l = [mii() for _ in range(r)]
  
  for *crt, price in l:
    cnt = 1e10
    for i in range(k):
      if crt[i] == 0:
        continue
      cnt = min(cnt, cap[i] // crt[i])
    
    mx = max(mx, cnt * price)
  
  p(mx)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()