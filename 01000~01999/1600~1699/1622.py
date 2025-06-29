"""
[1622: 공통 순열](https://www.acmicpc.net/problem/1622)

Tier: Silver 4 
Category: sorting, string
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = False
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
  while 1:
    try:
      a = inp()
      b = inp()
    except:
      break
  
    a = sorted(a)
    b = sorted(b)

    i = j = 0

    while i < len(a) and j < len(b):
      if a[i] < b[j]:
        i += 1
      elif a[i] > b[j]:
        j += 1
      else:
        p(a[i], end="")
        i += 1
        j += 1
    p()

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()