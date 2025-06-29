"""
[33663: 루미의 진정한™ 보라색 찾기](https://www.acmicpc.net/problem/33663)

Tier: Bronze 3 
Category: math, implementation, arithmetic
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
  h = mii()
  s = mii()
  v = mii()

  R, G, B = mii()

  M = max([R, G, B])
  m = min([R, G, B])

  V = M
  S = 255 * (V - m) / V

  H = -1

  if V == R:
    H = 60 * (G - B) / (V - m)
  elif V == G:
    H = 120 + 60 * (B - R) / (V - m)
  elif V == B:
    H = 240 + 60 * (R - G) / (V - m)
  
  if H < 0:
    H += 360
  
  if h[0] <= H <= h[1] and s[0] <= S <= s[1] and v[0] <= V <= v[1]:
    print("Lumi will like it.")
  else:
    print("Lumi will not like it.")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()