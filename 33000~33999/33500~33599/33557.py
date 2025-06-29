"""
[33557: 곱셈을 누가 이렇게 해 ㅋㅋ](https://www.acmicpc.net/problem/33557)

Tier: Silver 5 
Category: arithmetic, implementation, math, string
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
  a, b = isplit()

  A, B = int(a), int(b)

  result_a = A * B

  result_b = []

  a = a[::-1]
  b = b[::-1]

  for i in range(max(len(a), len(b))):
    if i < len(a) and i < len(b):
      result_b.append(str(int(a[i]) * int(b[i])))
    elif i < len(a):
      result_b.append(str(int(a[i])))
    else:
      result_b.append(str(int(b[i])))
  
  result_b = result_b[::-1]
  result_b = int("".join(result_b))
  # print(result_a, result_b)

  print(int(result_a == result_b))

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()