"""
[7586: Untied Airlines](https://www.acmicpc.net/problem/7586)

Tier: Bronze 2 
Category: data_structures, hash_set, implementation
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
  d = {
    'L': 120,
    'S': 150,
    'B': 150,
    'N': 40,
    'C': 160,
    'D': 100,
    'R': 100,
    'O': 100
  }
  
  while 1:
    name = inp()
    
    if name == '#':
      break
    
    chk = {}
    while 1:
      s = inp()
      
      if s == '00A':
        break

      a, b = s.split()
      chk[a] = chk.get(a, 0) + d.get(b, 0)
    
    
    ans = 0
    for _, sm in chk.items():
      if sm >= 200:
        ans += 1
    
    p(name, ans)
    
    
    


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()