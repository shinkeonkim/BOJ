"""
[33709: 치매예방수칙 3.3.3](https://www.acmicpc.net/problem/33709)

Tier: Bronze 1 
Category: arithmetic, math, parsing, string
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
  import re
  seperator = ".|:#"

  n = ii()
  s = inp()
  s = re.split(f"[{seperator}]", s)
  print(sum([int(i) for i in s]))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()