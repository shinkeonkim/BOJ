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

      
def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  for i in range(n):
    for j in range(n):
      if l[i][j] < 0:
        return (False, -1)

  cnt = 0
  for i in range(n):
    sm = 0

    for j in range(n):
      if i == j:
        continue

      sm += l[i][j]
    
    if sm > l[i][i]:
      return (False, -1)
    
    if sm < l[i][i]:
      cnt += 1

  if cnt > 0:
    return (True, cnt)

  return (False, -1)  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

    if ret[0]:
      p("YES")
      print(ret[1])
    else:
      p("NO")