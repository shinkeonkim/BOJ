"""
[32680: Sauna](https://www.acmicpc.net/problem/32680)

Tier: Bronze 1 
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
  n = ii()
  l = [mii() for i in range(n)]
  
  crt = l[0]

  for i in range(1, n):
    nxt = l[i]

    new_range = [max(crt[0], nxt[0]), min(crt[1], nxt[1])]

    if new_range[0] > new_range[1]:
      return "bad news"
    
    crt = new_range
  
  return "{} {}".format(crt[1] - crt[0] + 1, crt[0])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)