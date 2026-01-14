"""
[32945: 극한직업 - 영양사 선생님](https://www.acmicpc.net/problem/32945)

Tier: Gold 5 
Category: greedy, sorting, sweeping, difference_array
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
  l = sorted(mii(), reverse=True)

  t = []

  for i in range(n):
    t.append(i + l[i])
  
  d = list(set(t + [i for i in range(0, n)]))
  d.sort()

  dd = {}

  for i in range(len(d)):
    dd[d[i]] = i
  
  diff = [0] * (2 * n + 2)

  for i in range(n):
    diff[dd[i]] += 1
    diff[dd[i + l[i]]] -= 1
  
  for i in range(1, 2 * n + 2):
    diff[i] += diff[i - 1]
  
  print(max(diff))

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()