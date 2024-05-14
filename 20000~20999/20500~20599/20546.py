"""
[20546: 🐜 기적의 매매법 🐜](https://www.acmicpc.net/problem/20546)

Tier: Silver 5
Category: 구현
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(money, l):
  cnt = 0
  
  for price in l:
    if money >= price:
      buy = money // price
      cnt += buy
      money %= price
    
  return cnt * l[-1] + money


def g(money, l):
  cnt = 0

  for i in range(3, 14):
    if l[i - 3] < l[i - 2] < l[i - 1]:
      money += l[i] * cnt
      cnt = 0
    elif l[i - 3] > l[i - 2] > l[i - 1]:
      buy = money // l[i]
      cnt += buy
      money %= l[i]
  
  return cnt * l[-1] + money
      

def solve():
  money = ii()
  l = mii()
  
  A = f(money, l[::])
  B = g(money, l[::])
  
  if A > B:
    p("BNP")
  elif A < B:
    p("TIMING")
  else:
    p("SAMESAME")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
