"""
[32621: 동아리비 횡령](https://www.acmicpc.net/problem/32621)

Tier: Bronze 2 
Category: case_work, implementation, string
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
  # n+n 형식의 문자열인가 n 은 양의 정수

  s = inp()

  if "+" not in s:
    return False
  
  a, b = s.split("+")

  if a != b:
    return False

  a = int(a)
  b = int(b)

  
  if a > 0 and b > 0 and a == b:
    return True

  return False



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    if ret:
      print("CUTE")
    else:
      print("No Money")