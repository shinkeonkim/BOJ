"""
[33639: Candy Store](https://www.acmicpc.net/problem/33639)

Tier: Bronze 2 
Category: bruteforcing, implementation, string
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
  n, q = mii()

  l = [isplit() for _ in range(n)]

  cnt = {}
  d = {}

  for i in range(n):
    nickname = ""
    for j in l[i]:
      nickname += j[0]
    
    cnt[nickname] = cnt.get(nickname, 0) + 1
    d[nickname] = l[i]

  queries = [inp() for _ in range(q)]

  for query in queries:
    if query in cnt:
      if cnt[query] == 1:
        print(*d[query])
      else:
        print("ambiguous")
    else:
      print("nobody")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()