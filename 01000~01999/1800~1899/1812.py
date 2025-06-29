"""
[1812: 사탕](https://www.acmicpc.net/problem/1812)

Tier: Silver 4 
Category: bruteforcing, math
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
  l = [ii() for _ in range(n)]

  c = l[0]

  for i in range(1, n):
    if i % 2 == 1:
      c -= l[i]
    else:
      c += l[i]
  
  c //= 2

  print(c)

  for i in range(0, n - 1):
    c = l[i] - c
    print(c)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()