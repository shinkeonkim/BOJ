"""
[5599: カードの並び替え](https://www.acmicpc.net/problem/5599)

Tier: Silver 5 
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

cards = []
n = 0

def cut(k):
  global cards
  cards = cards[k:] + cards[:k]

def shuffle():
  global cards, n

  a = cards[:n]
  b = cards[n:]

  ret = []

  for i in range(n):
    ret.append(a[i])
    ret.append(b[i])
  
  cards = ret


def solve():
  global cards, n
  n = ii()
  m = ii()

  cards = [i for i in range(1, 2 * n + 1)]

  l = [ii() for _ in range(m)]
  
  for i in range(m):
    if l[i] == 0:
      shuffle()
    else:
      cut(l[i])
  
  for i in range(2 * n):
    print(cards[i])


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()