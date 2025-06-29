"""
[15027: Alien Sunset](https://www.acmicpc.net/problem/15027)

Tier: Bronze 1 
Category: arithmetic, bruteforcing, math
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

  mx_day_time = max(l[i][0] for i in range(n))

  def is_night(cur_time, day_time, start_day, end_day):
    tm = cur_time % day_time
    if start_day <= end_day:
      return tm <= start_day or tm >= end_day
    else:
      return tm <= start_day and tm >= end_day
    

  for t in range(1825 * mx_day_time+1):
    all_night = all(is_night(t, l[i][0], l[i][1], l[i][2]) for i in range(n))

    if all_night:
      print(t)
      break
  else:
    print("impossible")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()