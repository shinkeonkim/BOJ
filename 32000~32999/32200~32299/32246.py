"""
[32246: 빙고 막기](https://www.acmicpc.net/problem/32246)

Tier: Bronze 3 
Category: constructive
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

def tm_to_i(s):
  h,m = map(int, s.split(":"))
  return h*60+m

def solve():
  n = ii()
  l = [inp().split() for _ in range(n + 1)]
  
  cutoff_tm = tm_to_i(inp())
  
  teacher_tm  = 0
  
  for a, b in l:
    if b == "teacher":
      teacher_tm = tm_to_i(a)
      break
  
  ans = 0
  for a, b in l:
    if b == "student":
      tm = tm_to_i(a)
      if tm >= cutoff_tm and tm >= teacher_tm:
        ans += 1
  
  p(ans)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()