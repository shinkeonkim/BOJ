"""
[15183: Musical Chairs](https://www.acmicpc.net/problem/15183)

Tier: Silver 4 
Category: implementation, simulation
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
  n = int(input())

  people = [input() for _ in range(n)]

  R = int(input())

  for _ in range(R):
    S, M = map(int, input().split())

    ln = len(people)

    M %= ln

    people = people[-M:] + people[:-M]

    poped_person = people.pop(S - 1)

    print(f"{poped_person} has been eliminated.")
  
  people.sort()

  if len(people) == 1:
    print(f"{people[0]} has won.")
  else:
    print(f"Players left are {' '.join(people)}.")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
