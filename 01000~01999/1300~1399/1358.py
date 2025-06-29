"""
[1358: 하키](https://www.acmicpc.net/problem/1358)

Tier: Silver 4 
Category: geometry
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
  W, H, X, Y, P = mii()
  l = [mii() for _ in range(P)]

  def square_distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

  def is_inside(x, y):
    # 직사각형
    if X <= x <= X + W and Y <= y <= Y + H:
      return True

    # 왼쪽 반원
    center = (X, Y + H // 2)
    radius = H // 2
    if x <= X and square_distance(x, y, center[0], center[1]) <= radius ** 2:
      return True

    # 오른쪽 반원
    center = (X + W, Y + H // 2)
    if x >= X + W and square_distance(x, y, center[0], center[1]) <= radius ** 2:
      return True
    return False


  cnt = 0

  for x, y in l:
    if is_inside(x, y):
      cnt += 1
  
  print(cnt)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()