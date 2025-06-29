"""
[30619: 내 집 마련하기](https://www.acmicpc.net/problem/30619)

Tier: Silver 2 
Category: implementation, sorting
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
  l = mii()

  idxs = [0] * (n + 1)

  for i in range(n):
    idxs[l[i]] = i

  m = ii()
  
  for _ in range(m):
    a, b = mii()

    k = []
    l2 = l[::]

    for i in range(a, b + 1):
      k.append(idxs[i])
    
    k.sort()

    for i in range(len(k)):
      l2[k[i]] = a + i
    
    print(*l2)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()