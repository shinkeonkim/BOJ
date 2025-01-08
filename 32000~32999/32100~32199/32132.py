"""
[32132: PlayStation이 아니에요](https://www.acmicpc.net/problem/32132)

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
  n = ii()
  s = inp()
  
  ans = ""
  for i in range(n):
    if len(ans) < 2:
      ans += s[i]
    else:
      if ans[-2] == "P" and ans[-1] == "S":
        if s[i] in "45":
          continue
      ans += s[i]
      

  p(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()