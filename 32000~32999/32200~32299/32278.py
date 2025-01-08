"""
[32278: 선택 가능성이 가장 높은 자료형](https://www.acmicpc.net/problem/32278)

Tier: Bronze 4 
Category: implementation
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

  if -32768 <= n <= 32767:
    print("short")
  elif -2147483648 <= n <= 2147483647:
    print("int")
  else:
    print("long long")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()