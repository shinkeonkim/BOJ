"""
[31945: 정육면체의 네 꼭짓점](https://www.acmicpc.net/problem/31945)

Tier: Bronze 2 
Category: case_work, implementation
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
  d = [
    [0, 1, 2, 3],
    [2, 3, 6, 7],
    [4, 5, 6, 7],
    [0, 1, 4, 5],
    [0, 2, 4, 6],
    [1, 3, 5, 7]
  ]
  
  p("YES" if sorted(mii()) in d else "NO")


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()