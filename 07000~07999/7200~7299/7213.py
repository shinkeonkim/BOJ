"""
[7213: Akmuo, popierius, žirklės](https://www.acmicpc.net/problem/7213)

Tier: Bronze 1 
Category: greedy, implementation
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

def win(a, b):
  ret = 0
  for i in range(3):
    k = min(a[i], b[(i + 2) % 3]) # i로 (i + 2) % 3를 이김
    a[i] -= k
    b[(i + 2) % 3] -= k
    ret += k
  return ret

def tie(a, b):
  for i in range(3):
    k = min(a[i], b[i]) # 무승부
    a[i] -= k
    b[i] -= k

def lose(a, b):
  ret = 0
  for i in range(3):
    k = min(a[i], b[(i + 1) % 3]) # i로 (i + 1) % 3를 짐
    a[i] -= k
    b[(i + 1) % 3] -= k
    ret -= k
  return ret

def greedy_win(a, b):
  # 가위, 바위, 보
  ret = 0

  ret += win(a, b) # a가 이김
  tie(a, b) # 무승부
  ret += lose(a, b) # a가 짐

  return ret

def greedy_lose(a, b):
  ret = 0
  ret += lose(a, b) # a가 짐
  tie(a, b) # 무승부
  ret += win(a, b) # a가 이김
  return ret

def solve():
  A = mii()
  B = mii()

  a = greedy_win(A[::], B[::])
  b = greedy_lose(A[::], B[::])

  print(a)
  print(b)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
