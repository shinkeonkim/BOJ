"""
[33167: じゃんけん (Rock-Scissors-Paper)](https://www.acmicpc.net/problem/33167)

Tier: Bronze 3 
Category: implementation, math, string
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
  A = inp()
  B = inp()

  k = "RSP"

  a, b = 0, 0
  for i in range(n):
    if A[i] == B[i]:
      continue
    if A[i] == "R" and B[i] == "S":
      a += 1
    elif A[i] == "S" and B[i] == "P":
      a += 1
    elif A[i] == "P" and B[i] == "R":
      a += 1
    else:
      b += 1
  
  print(a, b)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()