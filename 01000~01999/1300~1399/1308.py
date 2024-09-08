"""
[1308: D-Day](https://www.acmicpc.net/problem/1308)

Tier: Silver 5 
Category: implementation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta, date

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
  a = date(*map(int,input().split()))
  b = date(*map(int,input().split()))
  
  if a.year + 1000 < b.year or \
    (a.year + 1000 == b.year and (a.month < b.month or (a.month == b.month and a.day <= b.day))):
    print("gg")
  else:
    print(f"D-{(b-a).days}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()