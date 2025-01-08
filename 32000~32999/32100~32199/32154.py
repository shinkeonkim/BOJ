"""
[32154: SUAPC 2024 Winter](https://www.acmicpc.net/problem/32154)

Tier: Bronze 5 
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

d = [
  ["11", "A B C D E F G H J L M"],
  ["9", "A C E F G H I L M"],
  ["9", "A C E F G H I L M"],
  ["9", "A B C E F G H L M"],
  ["8", "A C E F G H L M"],
  ["8", "A C E F G H L M"],
  ["8", "A C E F G H L M"],
  ["8", "A C E F G H L M"],
  ["8", "A C E F G H L M"],
  ["8", "A B C F G H L M"]
]

def solve():
  n = ii()
  p(d[n-1][0])
  p(d[n-1][1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()