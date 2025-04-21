"""
[15117: Latin Squares](https://www.acmicpc.net/problem/15117)

Tier: Bronze 1 
Category: implementation, string
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


def f(c):
  if '0' <= c <= '9':
    return int(c)
  return ord(c) - ord('A') + 10

def solve():
  n = ii()
  l = [inp() for _  in range(n)]

  for i in range(n):
    st = set(l[i])
    if len(st) != n:
      return "No"
    
    st = set()
    for j in range(n):
      st.add(l[j][i])
    if len(st) != n:
      return "No"
    
    for j in range(n):
      if f(l[i][j]) > n:
        return "No"
  

  for i in range(n - 1):
    if f(l[0][i]) >= f(l[0][i+1]):
      return "Not Reduced"
  
    if f(l[i][0]) >= f(l[i+1][0]):
      return "Not Reduced"
  
  return "Reduced"


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    print(ret)