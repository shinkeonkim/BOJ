"""
[16965: 구간과 쿼리](https://www.acmicpc.net/problem/16965)

Tier: Gold 5 
Category: graphs, graph_traversal, bfs
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

N = ii()
segs = [[]]
edges = defaultdict(list)

def moveable(s1, s2):
  return s2[0] < s1[0] < s2[1] or s2[0] < s1[1] < s2[1]
  

def add_seg(a, b):
  segs.append((a, b))
  
  for i in range(1, len(segs)):
    if moveable(segs[i], segs[-1]):
      edges[i].append(len(segs) - 1)

    if moveable(segs[-1], segs[i]):
      edges[len(segs) - 1].append(i)

def find_path(a, b):
  visited = [False] * len(segs)
  q = deque([a])
  while q:
    here = q.popleft()
    if here == b:
      return True
    for nxt in edges[here]:
      if not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
  return False

for _ in range(N):
  q, a, b = mii()
  
  if q == 1:
    add_seg(a, b)
  else:
    ret = find_path(a, b)
    print(int(ret))
