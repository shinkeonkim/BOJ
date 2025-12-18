"""
[27584: I Could Have Won](https://www.acmicpc.net/problem/27584)

Tier: Silver 5 
Category: bruteforcing, implementation, simulation, string
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
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  s = input()

  ans = []
  for win_standard in range(1, len(s) + 1):
    A = B = 0
    A_count = B_count = 0

    for i in s:
      if i == 'A':
        A += 1
      else:
        B += 1
      
      if A >= win_standard:
        A_count += 1
        A = 0
        B = 0
      elif B >= win_standard:
        B_count += 1
        A = 0
        B = 0
    
    if A_count > B_count:
      ans.append(win_standard)
  
  print(len(ans))
  print(*ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
