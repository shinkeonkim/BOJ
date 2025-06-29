"""
[14655: 욱제는 도박쟁이야!!](https://www.acmicpc.net/problem/14655)

Tier: Silver 5 
Category: ad_hoc, greedy
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

def f(n, round):
  ans = 0
  
  for i in range(0, n - 3):
    ans += abs(round[i])
  
  tmp = round[n - 3] + round[n - 2] + round[n - 1]
  
  ans = ans + max(-tmp, tmp)
  return ans


def g(n, round):
  ans = 0
  
  for i in range(0, n - 3):
    ans -= abs(round[i])
  
  tmp = round[n - 3] + round[n - 2] + round[n - 1]
  
  ans = ans + min(-tmp, tmp)
  return ans

def solve():
  n = ii()
  
  first_round = mii()
  second_round = mii()
  
  
  first_round = f(n, first_round)
  second_round = f(n, second_round)
  
  p(first_round, second_round)
  
  
  
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()