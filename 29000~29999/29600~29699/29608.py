"""
[29608: Диагональное преобладание](https://www.acmicpc.net/problem/29608)

Tier: Bronze 2 
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


def f(l):
  mx = -1
  for i in l:
    mx = max(mx, max(i))
  
  return mx >= 0

def g(n, l, sm):
  cnt = 0
  ret = True
  for i in range(n):
    if l[i][i] * 2 > sm[i]:
      cnt += 1

    if l[i][i] * 2 < sm[i]:
      ret = False
  return (cnt, ret)

      
def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  sm = [sum(i) for i in l]
  
  a = f(l)
  cnt, b = g(n, l, sm)
  
  if a and b:
    p("YES")
    p(cnt)
  else:
    p("NO")
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()