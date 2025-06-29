"""
[12537: Closing the Loop (Small)](https://www.acmicpc.net/problem/12537)

Tier: Silver 5 
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
  n = ii()
  l = isplit()

  R = []
  B = []
  for i in l:
    color = i[-1]
    number = int(i[:-1])

    if color == "R":
      R.append(number)
    else:
      B.append(number)
  
  R.sort(reverse=True)
  B.sort(reverse=True)

  if len(R) < len(B):
    R, B = B, R

  if len(R) == 0 or len(B) == 0:
    return 0
  
  ans = 0
  for i in range(len(B)):
    if i != 0:
      ans -= 1
    ans += R[i] + B[i] - 1
  
  ans -= 1

  return ans


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    p(f"Case #{t}: {ret}")