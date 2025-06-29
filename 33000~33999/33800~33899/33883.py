"""
[33883: Acentuación del idioma español](https://www.acmicpc.net/problem/33883)

Tier: Bronze 3 
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

def is_vowel(c):
  return c in "aeiou"

def solve():
  s = input()
  idx = []

  for i in range(len(s)):
    if is_vowel(s[i]):
      idx.append(i + 1)

  if s[-1] not in "ns" and not is_vowel(s[-1]):
    print(idx[-1] if len(idx) > 0 else -1)
  else:
    print(idx[-2] if len(idx) > 1 else -1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()