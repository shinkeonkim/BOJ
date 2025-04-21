"""
[29412: Огни светофора](https://www.acmicpc.net/problem/29412)

Tier: Bronze 3 
Category: implementation, simulation
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
  l = mii()
  # g, gb, y, r, ry = l
  T = ii()

  t = 0
  idx = 0
  crt = 0
  ans = [0, 0, 0] # R, Y, G

  while t < T:
    if crt >= l[idx]:
      idx += 1
      crt = 0
    idx %= 5

    if idx == 0:
      ans[2] += 1
    elif idx == 1:
      if crt % 2 == 0:
        ans[2] += 1
    elif idx == 2:
      ans[1] += 1
    elif idx == 3:
      ans[0] += 1
    elif idx == 4:
      ans[0] += 1
      ans[1] += 1
    crt += 1
    t += 1
  print(*ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()