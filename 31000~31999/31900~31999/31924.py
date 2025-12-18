"""
[31924: 현대모비스 특별상의 주인공은? 2](https://www.acmicpc.net/problem/31924)

Tier: Silver 5 
Category: implementation, bruteforcing
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


n = ii()
l = [input() for _ in range(n)]

target = "MOBIS"

cnt = 0

for i in l:
  cnt += i.count(target)
  cnt += i.count(target[::-1])
  # print(i, i.count(target), i.count(target[::-1]))
# print(cnt)

for j in range(n):
  k = ""
  for i in range(n):
    k += l[i][j]
  
  cnt += k.count(target)
  cnt += k.count(target[::-1])
  # print(k, k.count(target), k.count(target[::-1]))
# print(cnt)
for i in range(n):
  for j in range(n):
    k = ""
    y, x = i, j
    while 0 <= y < n and 0 <= x < n and len(k) < 5:
      k += l[y][x]
      x += 1
      y += 1
    
    cnt += k.count(target)
    cnt += k.count(target[::-1])
    
    k = ""
    y, x = i, j
    while 0 <= y < n and 0 <= x < n and len(k) < 5:
      k += l[y][x]
      y += 1
      x -= 1

    cnt += k.count(target)
    cnt += k.count(target[::-1])

print(cnt)