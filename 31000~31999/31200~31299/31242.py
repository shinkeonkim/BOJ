"""
[31242: ШАХМАТНА ДЪСКA](https://www.acmicpc.net/problem/31242)

Tier: Bronze 1 
Category: implementation, simulation
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
  l = [mii() for _ in range(4)]
  
  d = {}
  
  for i in range(4):
    for j in range(5):
      d[l[i][j]] = [i, j]
  
  for i in range(2, 21):
    prev = d[i-1]
    cur = d[i]
    
    if (abs(prev[0] - cur[0]) == 1 and abs(prev[1] - cur[1]) == 2) or (abs(prev[0] - cur[0]) == 2 and abs(prev[1] - cur[1]) == 1):
      continue
    else:
      print(i - 1)
      break
  else:
    print(20)
      
    


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()