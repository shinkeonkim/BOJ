"""
[32855: Which One is Larger](https://www.acmicpc.net/problem/32855)

Tier: Bronze 2 
Category: arithmetic, implementation, math, parsing, string
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
  a = input()
  b = input()

  _a = a.split(".")[0]
  _b = b.split(".")[0]

  tuple_a = [*map(int, a.split("."))]
  tuple_b = [*map(int, b.split("."))]

  if float(a) > float(b) and tuple_a > tuple_b:
    print(a)
  elif float(a) < float(b) and tuple_a < tuple_b:
    print(b)
  else:
    print(-1)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()