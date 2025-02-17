"""
[28786: Выстрел в голову](https://www.acmicpc.net/problem/28786)

Tier: Bronze 2 
Category: arithmetic, math
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
  SHOOT_TIME = 1 # 한발당 발사 시간
  n, m, a, b = mii() # n : 발사할 탄수, m: 탄창의 크기, a: 탄청의 재장전 시간, b: 탄창에 한발의 총알을 넣는 시간

  # n발을 발사하는데 걸리는 시간
  ans = n

  # 탄창을 꽉채우는 경우

  full = (n // m + (1 if n % m != 0 else 0)) * a

  # 모두 개별로

  individual = n * b

  k = min(full, individual)

  # 일단 탄창 단위는 다 하고, 나머지는 개별로

  collabo = (n // m) * a + (n % m) * b

  k = min(k, collabo)

  print(ans + k)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()