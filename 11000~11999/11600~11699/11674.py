"""
[11674: Identifying Map Tiles](https://www.acmicpc.net/problem/11674)

Tier: Silver 5 
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
  s = inp()

  level = len(s)

  l = 2 ** (level - 1)
  y, x = 0, 0

  for i in range(level):
    crt = int(s[i])
    dy = [0, 0, 1, 1]
    dx = [0, 1, 0, 1]

    y += dy[crt] * l
    x += dx[crt] * l
    l //= 2
  
  print(level, x, y)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()