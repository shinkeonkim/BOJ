"""
[33631: 1교시: 가정](https://www.acmicpc.net/problem/33631)

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
  l = mii()
  need = mii()

  Q = ii()
  cnt = 0

  for _ in range(Q):
    command, i = mii()

    if command == 1:
      for j in range(4):
        if l[j] < i * need[j]:
          print("Hello, siumii")
          break
      else:
        for j in range(4):
          l[j] -= i * need[j]
        cnt += i
        print(cnt)
    else:
      l[command - 2] += i
      print(l[command - 2])



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()