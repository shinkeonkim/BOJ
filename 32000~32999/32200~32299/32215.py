"""
[32215: 코드마스터 2024](https://www.acmicpc.net/problem/32215)

Tier: Bronze 4 
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
  n, m, k = mii()
  
  # n대의 컴퓨터, m개의 에디터 설치, 그중 k개의 컴퓨터에는 m개를 설치해놨다.
  
  print(k * m + (m if k < n else 0))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()