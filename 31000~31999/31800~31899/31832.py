"""
[31832: 팀명 정하기 2](https://www.acmicpc.net/problem/31832)

Tier: Bronze 2 
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


def is_valid(s):
  if len(s) > 10:
    return False

  num_cnt = 0
  
  for i in s:
    if '0' <= i <= '9':
      num_cnt += 1
  
  if len(s) == num_cnt:
    return False

  small, capital = 0, 0
  
  for i in s:
    if 'a' <= i <= 'z':
      small += 1
    
    if 'A' <= i <= 'Z':
      capital += 1
  
  if capital > small:
    return False

  return True


def solve():
  n = ii()
  l = [inp() for _ in range(n)]
  
  for i in l:
    if is_valid(i):
      p(i)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()