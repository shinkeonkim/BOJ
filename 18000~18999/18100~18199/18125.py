"""
[18125: 고양이 사료](https://www.acmicpc.net/problem/18125)

Tier: Bronze 1 
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


def A():
  s = """|>___/|     /}
| O O |    / }
( =0= )\"\"\"\"  \\
| ^  ____    |
|_|_/    ||__|"""
  
  p(s)
  

def B():
  s = """|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|"""

  p(s)


def solve():
  n, m = mii()
  
  l = [mii() for _ in range(m)]
  
  l2 = [mii() for _ in range(n)]
  
  
  mk = []
  
  for i in range(m - 1, -1, -1):
    tmp = []
    for j in range(0, n):
      tmp.append(l2[j][i])
    mk.append(tmp)
  
  
  for i in range(m):
    for j in range(n):
      if l[i][j] != mk[i][j]:
        A()
        return

  B()
        


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()