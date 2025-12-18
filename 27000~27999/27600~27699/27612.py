"""
[27612: Determining Nucleotide Assortments](https://www.acmicpc.net/problem/27612)

Tier: Silver 2 
Category: prefix_sum, sorting
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


def solve():
  s = input()
  n = len(s)

  A_counts = [0] * (n + 1)
  T_counts = [0] * (n + 1)
  G_counts = [0] * (n + 1)
  C_counts = [0] * (n + 1)

  for i in range(n):
    A_counts[i + 1] = A_counts[i] + (1 if s[i] == 'A' else 0)
    T_counts[i + 1] = T_counts[i] + (1 if s[i] == 'T' else 0)
    G_counts[i + 1] = G_counts[i] + (1 if s[i] == 'G' else 0)
    C_counts[i + 1] = C_counts[i] + (1 if s[i] == 'C' else 0)

  q = int(input())

  for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    d = {}

    d['A'] = A_counts[b + 1] - A_counts[a]
    d['T'] = T_counts[b + 1] - T_counts[a]
    d['G'] = G_counts[b + 1] - G_counts[a]
    d['C'] = C_counts[b + 1] - C_counts[a]

    d = sorted(d.items(), key=lambda x: (-x[1], 'ATGC'.index(x[0])))

    print(''.join(i[0] for i in d))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
