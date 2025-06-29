"""
[32365: Heavy-Light Composition](https://www.acmicpc.net/problem/32365)

Tier: Bronze 2 
Category: implementation, string
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
  n, m = mii()

  for _ in range(n):
    s = inp()
    d = {}
    for i in s:
      d[i] = d.get(i, 0) + 1
    
    k = [d[i] % 2 for i in s]

    ret = True
    for i in range(m - 1):
      if k[i] == k[i + 1]:
        ret = False
        break
    
    print("T" if ret else "F")



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()