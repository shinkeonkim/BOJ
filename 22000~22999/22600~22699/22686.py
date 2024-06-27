"""
[22686: Dance Dance Revolution](https://www.acmicpc.net/problem/22686)

Tier: Bronze 1 
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
  n = len(s)
  
  directions = [-1] * n

  for i in range(n):
    if s[i] == 'L':
      directions[i] = 0
    elif s[i] == 'R':
      directions[i] = 1
  
  for i in range(n - 1):
    if s[i] == s[i + 1]:
      return "No"

  st = -1
  
  for i in range(n):
    if directions[i] >= 0:
      st = i
      break
  
  crt = 1 - directions[st]
  for i in range(st + 1, n):
    if directions[i] >= 0:
      if crt != directions[i]:
        return "No"

    crt = 1 - crt

  return "Yes"


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    p(ret)