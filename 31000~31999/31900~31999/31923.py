"""
[31923: 마라탕후루](https://www.acmicpc.net/problem/31923)

Tier: Bronze 2
Category: bruteforcing, math
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
def sign(a): return 1 if a > 0 else (-1 if a < 0 else 0)

def solve():
  n, p, q = mii() # 꼬치의 개수, 1분마다 꽂는 딸기 / 샤인머스캣의 개수
  
  A = mii() # 꼬치마다 꽂혀 있는 딸기의 개수
  B = mii() # 꼬치마다 꽂혀 있는 샤인머스캣의 개수

  diff = p - q
  
  ans = []

  for i in range(n):
    crt = B[i] - A[i]

    if sign(crt) == sign(diff):
      if sign(crt) == sign(diff) == 0:
        ans.append(0)
        continue
      
      if (diff == 0 and abs(crt) > 0) or (abs(crt) % abs(diff) != 0):
        print("NO")
        return

      ans.append(abs(crt) // abs(diff))
    elif sign(crt) == 0:
      ans.append(0)
    else:
      print("NO")
      return


  print("YES")
  print(*ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()