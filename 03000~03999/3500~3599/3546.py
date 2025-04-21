"""
[3546: Headshot](https://www.acmicpc.net/problem/3546)

Tier: Bronze 1 
Category: math, probability
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
  s = inp()
  n = len(s)
  zero_cnt = s.count("0")

  a, b = 0, 0
  for i in range(n):
    if s[i] == '0':
      if s[(i+1)%n] == '0':
        a += 1
      else:
        b += 1
  
  shoot = (a, a + b)
  rotate = (zero_cnt, n)

  if shoot[0] * rotate[1] == shoot[1] * rotate[0]:
    print("EQUAL")
  elif shoot[0] * rotate[1] < shoot[1] * rotate[0]:
    print("ROTATE")
  else:
    print("SHOOT")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()