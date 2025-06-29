"""
[32516: 팰린드롬 판별하기 2](https://www.acmicpc.net/problem/32516)

Tier: Silver 4 
Category: ad_hoc, string
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
  s = inp()

  for i in range(n):
    if s[i] == '?' or s[n-i-1] == '?':
      continue

    if s[i] != s[n-i-1]:
      return 0
  
  ans = 0
  for i in range(n // 2):
    if s[i] == '?' and s[n-i-1] == '?':
      ans += 26
    elif s[i] == '?' or s[n-i-1] == '?':
      ans += 1
  
  return ans


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)