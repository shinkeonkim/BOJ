"""
[10509: Good morning!](https://www.acmicpc.net/problem/10509)

Tier: Silver 3 
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
  edges = {
    1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    2: [2, 3, 5, 6, 8, 9, 0],
    3: [3, 6, 9],
    4: [4, 5, 6, 7, 8, 9, 0],
    5: [5, 6, 8, 9, 0],
    6: [6, 9],
    7: [7, 8, 9, 0],
    8: [8, 9, 0],
    9: [9],
    0: [0]
  }

  available = set()

  def dfs(node, crt):
    available.add(int(crt))
    
    if len(crt) == 3:
      return
    
    for next_node in edges[node]:
      dfs(next_node, crt + str(next_node))
  
  for i in range(0, 10):
    dfs(i, str(i))
  
  n = int(input())

  available = sorted(available)

  for _ in range(n):
    k = int(input())
    ans = float('inf')
    for z in available:
      if abs(z - k) < abs(ans - k) :
        ans = z
  
    print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
