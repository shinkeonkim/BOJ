"""
[32371: 샷건](https://www.acmicpc.net/problem/32371)

Tier: Bronze 1 
Category: bruteforcing, implementation, string
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
  l = [inp() for _ in range(4)]
  s = inp()
  
  k = []
  
  for crt in s:
    for i in range(4):
      for j in range(len(l[i])):
        if l[i][j] == crt:
          k.append((i,j))
          break
  
  k.sort()
  
  print(l[k[4][0]][k[4][1]])
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()