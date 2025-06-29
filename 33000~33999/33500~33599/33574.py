"""
[33574: 끊임없는 정렬과 창조함으로](https://www.acmicpc.net/problem/33574)

Tier: Silver 4 
Category: implementation, sorting, simulation
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
  Q = ii()
  l = []

  while Q > 0:
    Q -= 1
    query = mii()

    if query[0] == 1:
      l.sort()
      if query[1] == 2:
        l.reverse()
    else:
      l = l[:query[1]] + [query[2]] + l[query[1]:]
  
  print(len(l))
  if l:
    print(*l)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()