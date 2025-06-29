"""
[1347: 미로 만들기](https://www.acmicpc.net/problem/1347)

Tier: Silver 2 
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
  n = ii()
  s = inp()

  l = [['#'] * 101 for _ in range(101)]

  x, y = 50, 50
  mn_x, mx_x = 50, 50
  mn_y, mx_y = 50, 50

  l[y][x] = '.'

  direction = 0

  dy = [1, 0, -1, 0]
  dx = [0, -1, 0, 1]

  for i in s:
    if i == 'R':
      direction += 1
      direction %= 4
    elif i == 'L':
      direction += 3
      direction %= 4
    else:
      x += dx[direction]
      y += dy[direction]

      l[y][x] = '.'

      mn_x = min(mn_x, x)
      mx_x = max(mx_x, x)
      mn_y = min(mn_y, y)
      mx_y = max(mx_y, y)
  
  for i in range(mn_y, mx_y + 1):
    for j in range(mn_x, mx_x + 1):
      p(l[i][j], end='')
    p()
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()