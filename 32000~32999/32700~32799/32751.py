"""
[32751: 햄버거](https://www.acmicpc.net/problem/32751)

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
  n = ii()
  a, b, c, d = mii()

  s = inp()

  if s[0] != 'a' or s[-1] != 'a':
    return False
  
  for i in range(n - 1):
    if s[i] == s[i + 1]:
      return False
  
  if s.count('a') > a or s.count('b') > b or s.count('c') > c or s.count('d') > d:
    return False

  return True


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

    if ret:
      print("Yes")
    else:
      print("No")