"""
[32802: Mouse Pursuit](https://www.acmicpc.net/problem/32802)

Tier: Bronze 2 
Category: arithmetic, implementation, math
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
  l = [isplit() for _ in range(n)]
  k = ii()

  ans = [0, 0]

  for command, *args in l:
    s, c, g = list(map(int, args))

    if command == 'MISS':
      c *= -1
      g *= -1

    if s <= k:
      ans[0] += c
      ans[1] += g
  
  print(*ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()