"""
[33674: 하늘에서 떨어지는 $N$개의 별](https://www.acmicpc.net/problem/33674)

Tier: Bronze 2 
Category: implementation, simulation
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
  N, D, K = mii()

  l = [0] + mii()

  ans = 0
  stars = [0] * (N + 1)

  for _ in range(D):
    chk = False
    for i in range(1, N + 1):
      if stars[i] + l[i] > K:
        chk = True
    
    if chk:
      ans += 1

      stars = [0] * (N + 1)
    
    for i in range(1, N + 1):
      stars[i] += l[i]

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()