"""
[29145: Можно и отдохнуть](https://www.acmicpc.net/problem/29145)

Tier: Bronze 2 
Category: arithmetic, math
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
  N = ii()
  s = inp()

  ans = 0
  
  s_cnt = 0
  l_cnt = 0

  for i in s:
    if '0' <= i <='9':
      ans += 1
    else:
      if i == 'K' and s_cnt > 0:
        ans += 1
        s_cnt -= 1
      elif i == 'R' and l_cnt > 0:
        ans += 1
        l_cnt -= 1
      else:
        if i == 'K' or i == 'R':
          break
        if i == 'S':
          s_cnt += 1
        if i == 'L':
          l_cnt += 1
  p(ans)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()