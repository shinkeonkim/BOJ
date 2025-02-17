"""
[26360: Basket](https://www.acmicpc.net/problem/26360)

Tier: Bronze 3 
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
  points_per_shot = int(input())
  shot_made = int(input())
  foul_committed = int(input())

  total_points = 0

  if shot_made == 1:
      total_points += points_per_shot

  if foul_committed == 1:
      if shot_made == 1:
          free_throw = int(input())
          if free_throw == 1:
              total_points += 1
      else:
          for _ in range(points_per_shot):
              free_throw = int(input())
              if free_throw == 1:
                  total_points += 1

  print(total_points)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()