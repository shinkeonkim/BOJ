"""
[5790: Log Books](https://www.acmicpc.net/problem/5790)

Tier: Bronze 2 
Category: math, string
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


def tm_to_min(s):
  h, m = s.split(":")
  h = int(h)
  m = int(m)
  return h * 60 + m

def solve():
  while 1:
    n = ii()
    if n == 0:
      break
    
    l = [isplit() for _ in range(n)]

    chk = True
    total_times = [0, 0, ]

    for tms in l:
      tms = [*map(tm_to_min, tms)]

      day = [tms[0], tms[1]]

      work_time = [tms[2], tms[3]]

      over_work_time = 0

      total_work_time = work_time[1] - work_time[0]

      over_work_time = max(0, min(day[0], work_time[1]) - work_time[0]) + max(0, work_time[1] - max(day[1], work_time[0]))

      if total_work_time > 2 * 60:
        chk = False

      total_times[0] += total_work_time

      if over_work_time * 2 >= total_work_time:
        total_times[1] += over_work_time
      
    
    if total_times[0] < 50 * 60:
      chk = False
    if total_times[1] < 10 * 60:
      chk = False

    if chk:
      print("PASS")
    else:
      print("NON")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()