"""
[2164: 카드2](https://www.acmicpc.net/problem/2164)

Tier: Silver 4 
Category: data_structures, queue
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

from collections import deque

def solve():
  n = ii()
  
  queue = deque([i for i in range(1, n+1)])
  
  while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
  
  print(queue[0])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()