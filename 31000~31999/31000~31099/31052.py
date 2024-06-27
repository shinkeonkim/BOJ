"""
[31052: Relocation](https://www.acmicpc.net/problem/31052)

Tier: Bronze 3 
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
  n, q = mii()
  
  positions = [0] + mii()
  
  for _ in range(q):
    q, a, b = mii()
    
    if q == 1:
      # a 회사를 b로 옮긴다.
      positions[a] = b
    else:
      # a회사, b회사 사이의 거리
      p(abs(positions[a] - positions[b]))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()