"""
[33026: LOL Lovers](https://www.acmicpc.net/problem/33026)

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
  s = inp()

  l_cnt = s.count("L")
  o_cnt = s.count("O")

  crt_l = 0
  crt_o = 0

  for i in s[:-1]:
    if i == "L":
      crt_l += 1
    elif i == "O":
      crt_o += 1

    left_l = l_cnt - crt_l
    left_o = o_cnt - crt_o

    if crt_l != left_l and crt_o != left_o:
      return crt_l + crt_o
    
  return -1


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)