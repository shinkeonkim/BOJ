"""
[31823: 악질 검거](https://www.acmicpc.net/problem/31823)

Tier: Bronze 1 
Category: implementation
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
  n, m = mii()
  ans = []
  ans_cnt = set()

  for _ in range(n):
    l = inp().split()
    name = l[-1]

    cnt = 0
    mx = 0
    for z in l[:-1]:
      if z == '.':
        cnt += 1
      else:
        cnt = 0
      mx = max(mx, cnt)

    ans_cnt.add(mx)
    ans.append((mx, name))
  
  print(len(ans_cnt))
  for a in ans:
    print(*a)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()