"""
[19941: 햄버거 분배](https://www.acmicpc.net/problem/19941)

Tier: Silver 3 
Category: greedy
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
  n , k = mii()
  s = list(inp()) # P: 사람, H: 햄버거
  
  cnt = 0
  
  for i in range(n):
    if s[i] == "P":
      for j in range(max(i-k, 0), min(i+k+1, n)):
        if s[j] == "H":
          s[j] = ""
          cnt += 1
          break
  
  p(cnt)
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()