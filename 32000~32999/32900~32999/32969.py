"""
[32969: 학술대회 참가신청](https://www.acmicpc.net/problem/32969)

Tier: Bronze 3 
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

A = ["social", "history", "language", "literacy"]
B = ["bigdata", "public", "society"]

def solve():
  s = inp()

  for i in A:
    if i in s:
      print("digital humanities")
      return
  for i in B:
    if i in s:
      print("public bigdata")
      return


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()