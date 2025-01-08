"""
[32515: BB84](https://www.acmicpc.net/problem/32515)

Tier: Bronze 3 
Category: implementation, string
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
  
  jung_base = inp()
  jung_key = inp()
  ian_base = inp()
  ian_key = inp()
  
  new_key = []
  
  for i in range(n):
    if jung_base[i] == ian_base[i]:
      if jung_key[i] == ian_key[i]:
        new_key.append(jung_key[i])
      else:
        print("htg!")
        return
  
  print("".join(new_key))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()