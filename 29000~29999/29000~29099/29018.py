"""
[29018: クレヨンの並べ替え](https://www.acmicpc.net/problem/29018)

Tier: Silver 5 
Category: implementation, sorting, string
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

def sort_order(ch):
  if 'a' <= ch <= 'z':
    return ord(ch) - ord('a')
  if 'A' <= ch <= 'Z':
    return ord(ch) - ord('A') + 26
  if '0' <= ch <= '9':
    return ord(ch) - ord('0') + 52

def solve():
  while 1:
    s = inp()

    if s == '#':
      break
    
    s = sorted(s, key=sort_order)
    s = ''.join(s)
    print(s)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()