"""
[9009: 피보나치](https://www.acmicpc.net/problem/9009)

Tier: Silver 1 
Category: greedy, math
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
  fib = [0, 1]
  for i in range(2, 46):
    fib.append(fib[i-1] + fib[i-2])
  fib = fib[2:]
  fib.reverse()

  n = ii()
  for i in range(n):
    num = ii()
    ans = []
    for f in fib:
      if f <= num:
        ans.append(f)
        num -= f
    print(*ans[::-1])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()