"""
[20493: 세상은 하나의 손수건](https://www.acmicpc.net/problem/20493)

Tier: Silver 4 
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
  step, total_time = mii()


  l = [inp().split() for _ in range(step)]

  direction = 0
  current_time = 0

  for i in range(step):
    tm = int(l[i][0])
    dir = l[i][1]

    duration = tm - current_time
    current_time = tm

    if dir == "left":
      direction = (direction + 3) % 4
    else:
      direction = (direction + 1) % 4
    
    l[i] = [duration, direction]
  
  l.append([total_time - current_time, direction])

  # print(l)

  current_point = [0, 0]
  dy = [0, -1, 0, 1]
  dx = [1, 0, -1, 0]
  direction = 0

  for duration, dir in l:
    current_point[0] += dy[direction] * duration
    current_point[1] += dx[direction] * duration
    direction = dir
  
  print(current_point[1], current_point[0])



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()