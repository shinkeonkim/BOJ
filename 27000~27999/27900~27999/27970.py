"""
[27970: OX](https://www.acmicpc.net/problem/27970)

Tier: Silver 1 
Category: ad_hoc, math
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = True
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

s = ""
n = 0
d = [1, 2]
MOD = 1000000007

def f(s, last_idx):
  while last_idx >= 0:
    if s[last_idx] == "O":
      break
    last_idx -= 1
  
  if(last_idx < 0):
    return 0
  
  if last_idx == 0:
    return 1
  
  k = d[last_idx]

  return (k + f(s, last_idx - 1)) % MOD

def solve():
  global s, n, d

  for i in range(2, 100001):
    d.append((d[-1] * 2) % MOD)

  s = inp()
  n = len(s)

  ret = f(s, n - 1)
  p(ret)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()