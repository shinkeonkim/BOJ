"""
[15029: Cued In](https://www.acmicpc.net/problem/15029)

Tier: Bronze 1 
Category: greedy, implementation, string
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
  color = {
    "red": 0,
    "yellow": 1,
    "green": 2,
    "brown": 3,
    "blue": 4,
    "pink": 5,
    "black": 6
  }
  ans = 0
  cnt = [0] * 7
  score = [1, 2, 3, 4, 5, 6, 7]
  
  for i in range(ii()):
    cnt[color[inp()]] += 1
  
  if cnt[0] == sum(cnt):
    p(1)
    return
  
  while cnt[0] > 0 and sum(cnt) != cnt[0]:
    crt = -1
    for i in range(6, 0, -1):
      if cnt[i] > 0:
        crt = i
        break    
    
    ans += score[crt]
    ans += score[0]
    cnt[0] -= 1
  
  if sum(cnt) != cnt[0]:
    for i in range(1, 7):
      ans += cnt[i] * score[i]
  
  p(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()