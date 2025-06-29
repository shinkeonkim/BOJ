"""
[15886: 내 선물을 받아줘 2](https://www.acmicpc.net/problem/15886)

Tier: Silver 3 
Category: graphs, string
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter

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

  ans = 0
  chk = [0] * n
  group = [i for i in range(n)]

  def find(a):
    if group[a] != a:
      group[a] = find(group[a])
    return group[a]

  def merge(a, b):
    a = find(a)
    b = find(b)

    if a == b:
      return

    group[b] = a


  for i in range(n):
    if chk[i]:
      continue

    ans += 1
    q = deque([i])
    grp = find(i)

    while q:
      cur = q.popleft()
      merge(cur, grp)

      if chk[cur]:
        continue

      chk[cur] = 1

      if s[cur] == 'E':
        q.append(cur + 1)
      else:
        q.append(cur - 1)
  
  for i in range(n):
    group[i] = find(i)
  
  print(len(set(group)))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()