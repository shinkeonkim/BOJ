"""
[30143: Cookie Piles](https://www.acmicpc.net/problem/30143)

Tier: Bronze 4 
Category: math
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
  n, a, d = mii()
  # n : 수열의 갯수
  # a : 시작 숫자
  # d : 공차
  
  # 전체 수열의 합
  
  print(n * a + n * (n-1) * d // 2)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()