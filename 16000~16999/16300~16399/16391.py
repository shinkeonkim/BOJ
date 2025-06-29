"""
[16391: Zebras and Ocelots](https://www.acmicpc.net/problem/16391)

Tier: Silver 5 
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
  l = [inp() == "Z" for _ in range(n)]

  cnt = 0

  while 1:
    if set(l) == {True}:
      break

    last_o = -1
    for i in range(n - 1, -1, -1):
      if l[i] == False:
        last_o = i
        break
    
    if last_o == -1:
      break
    
    l[last_o] = True

    for i in range(last_o + 1, n):
      if l[i] == True:
        l[i] = False
    cnt += 1

  p(cnt)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
