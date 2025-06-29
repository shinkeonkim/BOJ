"""
[30342: Picos](https://www.acmicpc.net/problem/30342)

Tier: Bronze 1 
Category: arithmetic, implementation, math, simulation
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
  n, m, t, k = mii()

  shower_turn = n // m + int(n % m != 0)

  buy_turn = k // t + int(k % t != 0)

  turn = min(shower_turn, buy_turn)

  ans = m * (k * turn - (t * (turn - 1) * turn) // 2)

  if shower_turn == turn and n % m != 0:
    ans -= (m - n % m) * (k - (turn - 1) * t)

  p(ans)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()