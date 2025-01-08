"""
[3969: My brother’s diary](https://www.acmicpc.net/problem/3969)

Tier: Bronze 1 
Category: implementation, math, string
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
  s = inp()
  d = {}

  for i in s:
    if i == ' ':
      continue
    d[i] = d.get(i, 0) + 1

  mx_cnt = max(d.values())

  ans = []

  for i in d:
    if d[i] == mx_cnt:
      ans.append(i)


  if len(ans) >= 2:
    print("NOT POSSIBLE")
    return
  
  ans = ans[0]

  # ans가 E가 되도록 변환

  diff = 26 - (ord('E') - ord(ans) + 26) % 26

  if diff == 26:
    diff = 0


  print(diff, end=" ")

  for i in s:
    if i == ' ':
      print(i, end="")
    else:
      print(chr((ord(i) - ord('A') - diff + 26) % 26 + ord('A')), end="")
  print()


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
