"""
[10997: 별 찍기 - 22](https://www.acmicpc.net/problem/10997)

Tier: Silver 2 
Category: implementation, recursion
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
from fractions import Fraction

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
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  n = int(input())
  
  if n == 1:
    print("*")
    return
  
  x_k = 1 + 4 * (n - 1)
  y_k = x_k + 2
  
  l = [[" "] * x_k for _ in range(y_k)]
  
  dy = [0, 1, 0, -1]
  dx = [-1, 0, 1, 0]
  crt_d = 0
  crt = [0, x_k - 1]
  l[crt[0]][crt[1]] = '*'
  
  while(1):
    chk_cnt = 0
    
    for d in range(4):
      ny = crt[0] + dy[d] * 2
      nx = crt[1] + dx[d] * 2
      
      if ny < 0 or nx < 0 or ny >= y_k or nx >= x_k:
        continue
      
      if l[ny][nx] == '*':
        chk_cnt += 1
    
    if chk_cnt == 4:
      break
    
    ny = crt[0] + dy[crt_d]
    nx = crt[1] + dx[crt_d]
    
    nny = crt[0] + dy[crt_d] * 2
    nnx = crt[1] + dx[crt_d] * 2
    
    if ny < 0 or nx < 0 or ny >= y_k or nx >= x_k:
      crt_d = (crt_d + 1) % 4
    elif (0 <= nny < y_k and 0 <= nnx < x_k) and l[nny][nnx] == '*':
      crt_d = (crt_d + 1) % 4
      
    crt = [crt[0] + dy[crt_d], crt[1] + dx[crt_d]]
    l[crt[0]][crt[1]] = '*'
  

  for i in l:
    s = ""
    for j in i:
      s += j
    s = s.rstrip()
    print(s)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
