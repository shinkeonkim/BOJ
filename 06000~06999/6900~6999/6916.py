"""
[6916: 0123456789](https://www.acmicpc.net/problem/6916)

Tier: Unrated
Category: 구현
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(chk):
  if chk[0]:
    p(" * * *")
  else:
    p()
  
  s1 = ""
  if chk[1] and chk[2]:
    s1 = "*     *"
  elif chk[1]:
    s1 = "*"
  else:
    s1 = "      *"

  for _ in range(3):
    p(s1)
  
  if chk[3]:
    p(" * * *")
  else:
    p()

  s2 = ""
  if chk[4] and chk[5]:
    s2 = "*     *"
  elif chk[4]:
    s2 = "*"
  else:
    s2 = "      *"

  for _ in range(3):
    p(s2)

  if chk[6]:
    p(" * * *")
  else:
    p()


def solve():
  d = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
  ]
  
  f(d[ii()])

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
