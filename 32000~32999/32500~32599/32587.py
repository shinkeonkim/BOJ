"""
[32587: Dragged-out Duel](https://www.acmicpc.net/problem/32587)

Tier: Bronze 3 
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
  me = inp()
  enemy = inp()
  
  a = b = 0
  
  r = "RSP"

  for i in range(n):
    if me[i] == enemy[i]:
      continue
    
    if (me[i] == "R" and enemy[i] == "S") or (me[i] == "S" and enemy[i] == "P") or (me[i] == "P" and enemy[i] == "R"):
      a += 1
    else:
      b += 1

  if a > b:
    print("victory")
  else:
    print("defeat")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()