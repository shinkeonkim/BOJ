"""
[29649: Верное выражение](https://www.acmicpc.net/problem/29649)

Tier: Bronze 2 
Category: arbitrary_precision, arithmetic, implementation, math
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

def f(num, base):
  ret = 0
  crt = 1

  while num > 0:
    ret += crt * (num % 10)
    crt *= base
    num //= 10

  return ret

def solve():
  a, c = input().split(" = ")
  
  flag = 0
  if "+" in a:
    a, b = a.split(" + ")
  elif "-" in a:
    a, b = a.split(" - ")
    flag = 1
  else:
    a, b = a.split(" * ")
    flag = 2
  
  mx = max([int(i) for i in a + b + c])
  
    
  a = int(a)
  b = int(b)
  c = int(c)
  
  ans = []
  
  for base in range(mx + 1, 11):
    if flag == 0:
      if f(a, base) + f(b, base) == f(c, base):
        ans.append(base)
    elif flag == 1:
      if f(a, base) - f(b, base) == f(c, base):
        ans.append(base)
    else:
      if f(a, base) * f(b, base) == f(c, base):
        ans.append(base)
  
  p(len(ans))
  p(*ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()