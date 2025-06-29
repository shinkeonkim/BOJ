"""
[6857: Cell-Phone Messaging](https://www.acmicpc.net/problem/6857)

Tier: Bronze 1 
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
  while 1:
    s = input()

    if s == "halt":
      break

    l = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    prev = -1
    ans = 0

    for ch in s:
      idx = -1
      cnt = -1

      for i in range(len(l)):
        if ch in l[i]:
          idx = i
          cnt = l[i].index(ch) + 1
          break
      
      if prev == idx:
        ans += 2
      ans += cnt
      prev = idx
    print(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()