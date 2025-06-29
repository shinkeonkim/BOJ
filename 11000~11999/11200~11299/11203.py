"""
[11203: Numbers On a Tree](https://www.acmicpc.net/problem/11203)

Tier: Silver 5 
Category: math, trees
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

  if " " in s:
    h, command = s.split()
    h = int(h)
  else:
    h = int(s)
    command = ""

  index = 1
  
  for i in range(0, len(command)):
    if command[i] == 'L':
      index = index * 2 - 1
    else:
      index = index * 2
  
  cr_h = len(command)

  start = 0

  for i in range(0, h - cr_h):
    start += 2 ** (h - i)
  h_range = range(start + 1, start + 2 ** cr_h + 1)
  
  print(h_range[-index])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()