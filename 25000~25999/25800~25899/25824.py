"""
[25824: 빠른 오름차순 메시지 전달](https://www.acmicpc.net/problem/25824)

Tier: Silver 1 
Category: bruteforcing, backtracking
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

ans = float('inf')

def solve():
  global ans
  costs = [mii() for _ in range(12)]
  
  def dfs(group, node, cost):
    global ans
    extra_node = (set([2 * group, 2 * group + 1]) - {node}).pop()
    cost += costs[node][extra_node]
  
    if group == 5:
      ans = min(ans, cost)
      return
    
    nxt_group = group + 1
    nxt_nodes = [2 * nxt_group, 2 * nxt_group + 1]
    
    for nxt in nxt_nodes:
      dfs(nxt_group, nxt, cost + costs[extra_node][nxt])
  
  dfs(0, 0, 0)
  dfs(0, 1, 0)
  
  print(ans)
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
