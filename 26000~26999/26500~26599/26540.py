"""
[26540: Bloom](https://www.acmicpc.net/problem/26540)

Tier: Bronze 1 
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
  l = [mii() for _ in range(n)]
  dd = ii()
  ans = 0

  for i in range(n):
    day = dd
    duration = l[i][:-1]
    back_point = l[i][-1]

    d = sum(duration)

    if back_point < 0:
      if d <= day:
        ans += 1
    else:
      d2 = sum(duration[back_point:])

      if d <= day:
        day -= d

        if day == 0 or d2 == 0 or day % d2 == 0:
          ans += 1


  return ans        



if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(ret)