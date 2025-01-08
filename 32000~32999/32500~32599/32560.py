"""
[32560: Amalgram](https://www.acmicpc.net/problem/32560)

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


def solve():
  a = list(inp())
  b = list(inp())
  
  a.sort()
  b.sort()
  
  k = []
  
  i = j = 0
  
  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      k.append(a[i])
      i += 1
      j += 1
    elif a[i] < b[j]:
      k.append(a[i])
      i += 1
    else:
      k.append(b[j])
      j += 1
  
  while i < len(a):
    k.append(a[i])
    i += 1

  while j < len(b):
    k.append(b[j])
    j += 1
  
  p("".join(k))  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()