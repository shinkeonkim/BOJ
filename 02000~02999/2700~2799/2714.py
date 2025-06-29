"""
[2714: 문자를 받은 승환이](https://www.acmicpc.net/problem/2714)

Tier: Silver 3 
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


def f(r, c, l):
  codes = []

  code = ""

  current = (0, 0)
  chk = [[0] * c for _ in range(r)]
  dx = [1, 0, -1, 0]
  dy =[0, 1, 0, -1]
  d = 0

  for _ in range(r * c):
    y, x = current

    chk[y][x] = 1
    code += l[y][x]


    ny, nx = y + dy[d], x + dx[d]
    if ny >= r or nx >= c or chk[ny][nx]:
      d = (d + 1) % 4
    ny, nx = y + dy[d], x + dx[d]

    current = (ny, nx)
  
  codes = []

  for i in range(0, len(code), 5):
    t = code[i:i+5]
    t = t + "0" * (5 - len(t))
    codes.append(int(t, 2))
  
  ret = ""

  for c in codes:
    if c == 0:
      ret += " "
    else:
      ret += chr(64 + c)
  print(ret.strip())


def solve():
  r, c, txt = isplit()

  r = int(r)
  c = int(c)

  l = []

  for i in range(0, len(txt), c):
    l.append(txt[i:i+c])
  
  f(r, c, l)

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()