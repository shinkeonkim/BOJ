"""
[5947: Book Club](https://www.acmicpc.net/problem/5947)

Tier: Bronze 1 
Category: bruteforcing, implementation
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
  n, nq, p = mii()
  l = [mii() for _ in range(n)]

  questions = [mii() for _ in range(p)]

  crt = [i for i in range(n)]

  for a, b in questions:
    a -= 1

    nxt = []

    for i in crt:
      if l[i][a] == b:
        nxt.append(i)

    crt = nxt

  print(len(crt))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()