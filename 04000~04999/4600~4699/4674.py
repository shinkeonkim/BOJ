"""
[4674: Do the Untwist](https://www.acmicpc.net/problem/4674)

Tier: Silver 4 
Category: math, implementation, string
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

def to_num(c):
  if c == '_':
    return 0
  
  if c == '.':
    return 27

  return ord(c) - ord('a') + 1


def to_char(n):
  if n == 0:
    return '_'
  
  if n == 27:
    return '.'

  return chr(ord('a') + n - 1)


def solve():
  while 1:
    s = input()

    if s == '0':
      break

    key, ciphercode = s.split()
    key = int(key)
    n = len(ciphercode)

    plaincode = [""] * n

    for i in range(n):
      idx = (key * i) % n
      c = ciphercode[i]

      plaincode[idx] = to_char((to_num(c) + i) % 28)
    
    plaincode = "".join(plaincode)
    print(plaincode)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
