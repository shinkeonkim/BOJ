"""
[32777: 가희와 서울 지하철 2호선](https://www.acmicpc.net/problem/32777)

Tier: Bronze 3 
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
  start, end = mii()

  if start < end:
    a_dis = end - start
    b_dis = 43 - end + start
  else:
    a_dis = 43 - start + end
    b_dis = start - end
  
  if a_dis < b_dis:
    print("Inner circle line")
  elif a_dis > b_dis:
    print("Outer circle line")
  else:
    print("Same")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()