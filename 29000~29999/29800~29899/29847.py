"""
[29847: Character Frequencies](https://www.acmicpc.net/problem/29847)

Tier: Bronze 2 
Category: data_structures, hash_set, implementation, string
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
  d = {}
  for _ in range(n):
    s = sys.stdin.readline()
    for c in s:
      if c == ' ' or c == '\n':
        continue
      if c in d:
        d[c] += 1
      else:
        d[c] = 1

  for k in sorted(d.keys()):
    p(k, d[k])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()