"""
[32292: ABB to BA (Easy)](https://www.acmicpc.net/problem/32292)

Tier: Silver 5 
Category: bruteforcing, implementation, string
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

ret = []

def add(c):
  global ret

  ret.append(c)

  if len(ret) >= 3 and ret[-3:] == ['A', 'B', 'B']:
    ret.pop()
    ret.pop()
    ret.pop()
    add('B')
    add('A')

def solve():
  global ret

  ret = []

  n = ii()
  s = inp()

  for i in range(n):
    add(s[i])
  
  return "".join(ret)

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    print(solve())
