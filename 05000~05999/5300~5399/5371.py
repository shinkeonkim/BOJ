"""
[5371: Annoying Mosquitos](https://www.acmicpc.net/problem/5371)

Tier: Bronze 1 
Category: bruteforcing, implementation
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
  n = ii()
  target = [mii() for _ in range(n)]
  
  m = ii()
  hits = [mii() for _ in range(m)]

  chk = [0] * n
  for y, x in hits:
    for i in range(n):
      if abs(target[i][0] - y) <= 50 and abs(target[i][1] - x) <= 50:
        chk[i] = 1
  
  p(sum(chk))
    


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
