"""
[32767: 계산기가 필요해](https://www.acmicpc.net/problem/32767)

Tier: Bronze 2 
Category: implementation
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
  # 연산자 우선순위와 상관없이 s 문자열에 주어지는 순서대로 계산한다.

  s = inp().split()

  ret = float(s[0])

  for i in range(1, len(s), 2):
    if s[i] == "+":
      ret += float(s[i+1])
    elif s[i] == "-":
      ret -= float(s[i+1])
    elif s[i] == "*":
      ret *= float(s[i+1])
    elif s[i] == "/":
      ret /= float(s[i+1])

  template = f"""=================
|SASA CALCULATOR|
|{ret:15.3f}|
-----------------
|               |
| AC         /  |
| 7  8  9    *  |
| 4  5  6    -  |
| 1  2  3    +  |
|    0  .    =  |
================="""
  
  print(template)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()