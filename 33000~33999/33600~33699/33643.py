"""
[33643: Keys, Phone, Wallet](https://www.acmicpc.net/problem/33643)

Tier: Bronze 2 
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
  k = ["keys", "phone", "wallet"]
  l = set([inp() for _ in range(n)])
  
  for i in l:
    if i in k:
      k.remove(i)

  if len(k) == 0:
    print("ready")
  else:
    print(*k, sep="\n")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()