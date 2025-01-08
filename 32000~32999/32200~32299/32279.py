"""
[32279: 수열의 비밀 (Easy)](https://www.acmicpc.net/problem/32279)

Tier: Bronze 2 
Category: implementation, math
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
  p, q, r, s = mii()
  a = ii()
  
  l =[0] * (n+1)
  
  l[1] = a
  
  for i in range(2, n+1):
    if i % 2 == 0:
      l[i] = l[i // 2] * p + q
    else:
      l[i] = r * l[i // 2] + s
  
  print(sum(l))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()