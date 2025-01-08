"""
[32626: SPC에 가는 길](https://www.acmicpc.net/problem/32626)

Tier: Bronze 2 
Category: ad_hoc, case_work
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
  start = mii()
  end = mii()
  obstacle = mii()
  
  # 직선으로 이동하는 중에 장애물을 피해 방향 전환하는 최소 횟수
  # 거리는 최소가 아니어도 된다.
  
  # 1. 시작점과 도착점이 같은 경우 -> 0
  if start == end:
    return 0

  
  # 2. 시작점과 도착점이 일직선 상에 있고 장애물이 없는 경우 -> 0
  # 3. 시작점과 도착점이 일직선 상에 있고 장애물이 있는 경우 -> 2
  
  if start[0] == end[0] or start[1] == end[1]:
    if start[0] == end[0] and start[0] == obstacle[0] and min(start[1], end[1]) < obstacle[1] < max(start[1], end[1]):
      return 2
    if start[1] == end[1] and start[1] == obstacle[1] and min(start[0], end[0]) < obstacle[0] < max(start[0], end[0]):
      return 2
    
    return 0

  # 4. 시작점과 도착점이 일직선 상에 있지 않은 경우 -> 1
  return 1


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    
    print(ret)