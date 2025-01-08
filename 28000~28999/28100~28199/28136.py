"""
[28136: 원, 탁!](https://www.acmicpc.net/problem/28136)

Tier: Silver 5 
Category: greedy, implementation
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

  cnt = 1
  crt = l[0]

  for i in range(1, n):
    if crt < l[i]:
      crt = l[i]
    else:
      cnt += 1
      crt = l[i]
  
  if l[-1] < l[0]:
    cnt -= 1
  
  p(cnt)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()