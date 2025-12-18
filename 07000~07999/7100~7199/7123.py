"""
[7123: Vanaisa lotomängud](https://www.acmicpc.net/problem/7123)

Tier: Bronze 1 
Category: implementation, math
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from functools import reduce, lru_cache
from operator import itemgetter, attrgetter, mul, add, sub, truediv
from typing import List, Tuple, Dict, Set, Any, Union

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
	
# 1.	할아버지가 전체적으로 복권에 당첨된 금액이 지출한 금액보다 많은지, 적은지, 또는 같은지를 판단합니다.
# 2.	하루 동안 가장 큰 손실을 본 날을 찾습니다.
# 3.	연속된 며칠 간 가장 큰 손실을 본 기간을 찾습니다.

def solve():
  n = ii()
  l = [mii() for _ in range(n)] # cost, price
  l = [i[1] - i[0] for i in l] # profit
  
  total = sum(l)

  if total == 0:
    print("NULLIS")
  elif total > 0:
    print("PLUSSIS")
  else:
    print("MIINUSES")
  
  max_loss = min(l)

  if max_loss >= 0:
    print("0 0")
  else:
    idx = l.index(max_loss)
    print(idx + 1, -max_loss)

  max_period_loss = 0
  start = -1
  end = -1

  for i in range(n):
    for j in range(i + 1, n):
      period_loss = sum(l[i:j+1])
      if period_loss < max_period_loss:
        max_period_loss = period_loss
        start = i + 1
        end = j + 1

  if max_period_loss == 0:
    print("0 0")
  else:
    print(start, end, -max_period_loss)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
