"""
[4566: Is the Name of This Problem](https://www.acmicpc.net/problem/4566)

Tier: Bronze 1 
Category: parsing, string
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
  while 1:
    s = inp()

    if s == "END":
      break
      
    if s.count('"') != 2:
      print("not a quine")
      continue
    
    if s.count('" ') != 1:
      print("not a quine")
      continue

    if s[0] != '"':
      print("not a quine")
      continue

    a, b = s.split('" ')
    a = a[1:]

    if a != b:
      print("not a quine")
      continue

    print(f"Quine({b})")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()