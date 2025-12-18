"""
[3986: 좋은 단어](https://www.acmicpc.net/problem/3986)

Tier: Silver 4 
Category: data_structures, stack
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

def is_good_word(word: str) -> bool:
  stack = []

  for ch in word:
    if stack and stack[-1] == ch:
      stack.pop()
    else:
      stack.append(ch)

  return not stack

def solve():
  words = [inp() for _ in range(ii())]
  print(sum([1 for word in words if is_good_word(word)]))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
