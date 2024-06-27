"""
[7245: Kurjeris](https://www.acmicpc.net/problem/7245)

Tier: Bronze 2 
Category: implementation, simulation
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
  n, m = mii()
  
  l = [mii() for _ in range(m)]
  
  # 접수 시간, 얻는 이득, 걸리는 시간 목록
  
  tm = [0] * n
  benefit = [0] * n
  
  for current_time, price, *times in l:
    crt = -1
    min_arrive_time = 1e20
  
    for idx in range(n):
      if tm[idx] > current_time:
        continue
      
      arrive_time = times[idx] + current_time
      
      if min_arrive_time > arrive_time:
        min_arrive_time = arrive_time
        crt = idx
    
    if crt != -1:
      benefit[crt] += price
      tm[crt] = min_arrive_time
  
  p(*benefit)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()