"""
[18230: 2xN 예쁜 타일링](https://www.acmicpc.net/problem/18230)

Tier: Silver 1 
Category: greedy, sorting
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
  n, a, b = mii()

  one = mii()
  two = mii()

  one.sort(reverse=True) # 2 x 1
  two.sort(reverse=True) # 2 x 2


  l = one[:n]
  l2 = []

  left_cnt = n - len(l)

  if left_cnt % 2:
    l.pop()
    left_cnt += 1
  
  left_cnt //= 2

  # print(left_cnt)
  l2 = two[:left_cnt]


  i = len(l) - 1
  j = left_cnt

  while i > 0 and j < len(two):
    if l[i] + l[i-1] <= two[j]: 
      l[i] = l[i - 1] = 0
      l2.append(two[j])
      i -= 2
      j += 1
    else:
      break

  print(sum(l) + sum(l2))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

