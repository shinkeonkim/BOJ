"""
[24993: KIARA is a Recursive Acronym](https://www.acmicpc.net/problem/24993)

Tier: Bronze 1 
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
  n = ii()
  l = [inp() for _ in range(n)]
  
  chk = {}
  
  for i in range(65, 91):
    chk[chr(i)] = False
  
  for i in l:
    chk[i[0]] = True
  
  for i in l:
    for j in i:
      if not chk[j]:
        break
    else:
      p("Y")
      return
  
  p("N")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()