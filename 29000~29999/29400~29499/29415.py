"""
[29415: Треугольник](https://www.acmicpc.net/problem/29415)

Tier: Bronze 2 
Category: math
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
  area = ii()
  area *= 2
  ans = 0

  for width in range(1, area + 1):
    height = area // width

    if height < width:
      break

    if area % width != 0:
      continue
    
    diagonal = sqrt(width ** 2 + height ** 2)

    if diagonal == int(diagonal):
      ans += 1
  
  print(ans)




if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()