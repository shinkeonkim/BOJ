"""
[23028: 5학년은 다니기 싫어요](https://www.acmicpc.net/problem/23028)

Tier: Silver 5 
Category: greedy, implementation
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
  n, A, B = mii()

  l = [mii() for _ in range(10)]

  # l.sort(key = lambda x: (-x[0], -x[1]))

  for a, b in l[:(8 - n)]:
    c = min(a, 6)
    d = min(6 - c, b)

    A += c * 3
    B += (c + d) * 3

  if A >= 66 and B >= 130:
    print("Nice")
  else:
    print("Nae ga wae")



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()