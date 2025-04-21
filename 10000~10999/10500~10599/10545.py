"""
[10545: 뚜기뚜기메뚜기](https://www.acmicpc.net/problem/10545)

Tier: Bronze 1 
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


def solve():
  org = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
  d = {}
  for i in range(10):
    for j in org[i]:
      d[j] = i
  cnt = {}
  for i in range(10):
    for j in range(len(org[i])):
      cnt[org[i][j]] = j + 1

  l = mii()
  s = inp()

  key_map = {}
  for i in range(1, 10):
    key_map[l[i - 1]] = i

  prev = 0
  ans = ""

  for i in s:
    crt = key_map[d[i]]

    if prev == crt:
      ans += "#"
    
    ans += cnt[i] * str(crt)
    prev = crt
  print(ans)
    

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()