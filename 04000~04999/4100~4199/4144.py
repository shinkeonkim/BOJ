"""
[4144: Alien Communicating Machines](https://www.acmicpc.net/problem/4144)

Tier: Bronze 1 
Category: implementation, math
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

def num(c):
  if c.isdigit():
    return int(c)
  return ord(c) - ord('A') + 10

def num_to_char(n):
  if n < 10:
    return str(n)
  return chr(n - 10 + ord('A'))


def x_to_y_base(x, y, n):
  result = 0

  n1 = reversed(n)

  crt = 1
  for i in n1:
    result += num(i) * crt
    crt *= x
  
  result_str = ""
  while result > 0:
    result_str = num_to_char(result % y) + result_str
    result //= y
  
  if result_str == "":
    result_str = "0"
  
  return result_str


def solve():
  a, b, k = isplit()
  a = int(a)
  b = int(b)

  print(x_to_y_base(a, b, k))


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
