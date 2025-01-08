"""
[26336: Are We Stopping Again?](https://www.acmicpc.net/problem/26336)

Tier: Bronze 3 
Category: bruteforcing, math
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
  A, B, C = mii()
  
  # A: 총 주행 거리
  # B: 주유소에 얼마나 자주 들렀는지(마일)
  # C: 그가 음식을 먹으러 멈추는 빈도(마일)

  
  # 멈춘 횟수
  print(A, B, C)
  A -= 1
  print(A // B + A // C - A // (B * C // gcd(B, C)))


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()