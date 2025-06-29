"""
[33869: 일기 암호화하기](https://www.acmicpc.net/problem/33869)

Tier: Bronze 2 
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
  key = inp()
  s = inp()

  l = []
  for i in key:
    if i in l:
      continue
    l.append(i)
  
  for i in range(ord('A'), ord('Z') + 1):
    if chr(i) not in l:
      l.append(chr(i))
  
  for i in s:
    idx = ord(i) - ord('A')
    p(l[idx], end="")
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()