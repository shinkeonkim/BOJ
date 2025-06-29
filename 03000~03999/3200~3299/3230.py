"""
[3230: 금메달, 은메달, 동메달은 누가?](https://www.acmicpc.net/problem/3230)

Tier: Silver 5 
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
  n, m = mii()

  l = [[ii(), i] for i in range(n)]

  new_l = []
  for crt_rank, idx in l:
    crt_rank = crt_rank - 1
    new_l = new_l[:crt_rank] + [idx] + new_l[crt_rank:]
  
  
  l2 = [[ii(), new_l[m - i - 1]] for i in range(m)]

  new_l2 = []

  for crt_rank, idx in l2:
    crt_rank = crt_rank - 1
    new_l2 = new_l2[:crt_rank] + [idx] + new_l2[crt_rank:]
  
  for i in range(3):
    print(new_l2[i] + 1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()