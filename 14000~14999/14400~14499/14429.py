"""
[14429: 배스킨라빈스 31](https://www.acmicpc.net/problem/14429)

Tier: Bronze 1 
Category: game_theory, implementation, math
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
  l = [mii() for _ in range(n)]

  mn = 1e9
  ans = -1
  for idx, z in enumerate(l):
    j, m = z
    r = (j - 1) % (1 + m)
    # print(r)

    k = j - 1 - r

    turn = k // (1 + m) * 2 + 2

    if mn > turn:
      mn = turn
      ans = idx + 1
  
  p(ans, mn)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()