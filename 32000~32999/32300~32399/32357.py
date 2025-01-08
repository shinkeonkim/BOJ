"""
[32357: 더블팰린드롬](https://www.acmicpc.net/problem/32357)

Tier: Bronze 1 
Category: ad_hoc, implementation, math, string
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
  l = [inp() for _ in range(n)]
  
  palindrom_cnt = 0
  
  for s in l:
    if s == s[::-1]:
      palindrom_cnt += 1
  
  print(palindrom_cnt * (palindrom_cnt - 1))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()