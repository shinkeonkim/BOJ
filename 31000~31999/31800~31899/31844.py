"""
[31844: 창고지기](https://www.acmicpc.net/problem/31844)

Tier: Bronze 2 
Category: implementation, string
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

  robot = s.index('@')  
  box = s.index('#')
  target = s.index('!')
  
  if robot < box < target:
    p(target - robot - 1)
  elif target < box < robot:
    p(robot - target - 1)
  else:
    p(-1)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()