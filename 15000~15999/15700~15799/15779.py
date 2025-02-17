"""
[15779: Zigzag](https://www.acmicpc.net/problem/15779)

Tier: Silver 5 
Category: bruteforcing, implementation
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


def is_zig_zag(l): # l's length is 3
  if l[0] <= l[1] <= l[2]: return False
  if l[0] >= l[1] >= l[2]: return False
  return True


def solve():
  n = ii()
  l = mii()

  ans = 2

  crt = 0
  for i in range(1, n-1):
    if is_zig_zag(l[i-1:i+2]):
      crt += 1
      ans = max(ans, crt + 2)
    else:
      crt = 0
  print(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()