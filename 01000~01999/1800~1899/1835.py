"""
[1835: 카드](https://www.acmicpc.net/problem/1835)

Tier: Silver 4 
Category: implementation, data_structures, simulation, deque
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
  n = ii()
  l = [0 for _ in range(n)]

  crt = 0
  for i in range(1, n + 1):

    move_cnt = 0
    while move_cnt < i:
      crt = (crt + 1) % n
      if l[crt] == 0:
        move_cnt += 1  
    
    l[crt] = i

    if i == n:
      break
    move_cnt = 0
    while move_cnt < 1:
      crt = (crt + 1) % n
      if l[crt] == 0:
        move_cnt += 1
  print(*l)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()