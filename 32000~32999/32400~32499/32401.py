"""
[32401: ANA는 회문이야](https://www.acmicpc.net/problem/32401)

Tier: Bronze 2 
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
  n = ii()
  s = inp()
  
  a_chk = False
  n_chk = False
  ans = 0
  
  # ANA 를 찾아라
  
  for i in s:
    if i == 'A' and not a_chk:
      a_chk = True
    
    if i == 'N':
      if a_chk:
        n_chk = True
        a_chk = False
      else:
        a_chk = False
        n_chk = False
    
    if i == 'A' and n_chk:
      ans += 1
      a_chk = True
      n_chk = False
    
    if i == 'A' and not n_chk:
      a_chk = True

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()