"""
[32090: シンプルなエディタ](https://www.acmicpc.net/problem/32090)

Tier: Bronze 2 
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
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    
    s = ""
    crt = 0
    
    for _ in range(n):
      command, c = isplit()
      
      if command == "INSERT":
        s = s[:crt] + c + s[crt:]
        crt += 1
      elif command == "LEFT":
        crt = max(0, crt-1)
      else:
        crt = min(len(s), crt+1)
      
      # p(s, crt)
    p(s)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()