"""
[31859: SMUPC NAME](https://www.acmicpc.net/problem/31859)

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


def solve():
  n, s = input().split()
  n = int(n)

  st = set()

  cnt = 0
  s2 = ""
  for i in s:
    if i in st:
      cnt += 1
      continue
    s2 += i
    st.add(i)
  
  print("smupc_" + (str(1906+n) + s2 + str(cnt + 4))[::-1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()