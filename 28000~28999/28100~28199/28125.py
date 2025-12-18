"""
[28125: 2023 아주머학교 프로그래딩 정시머힌](https://www.acmicpc.net/problem/28125)

Tier: Silver 4 
Category: implementation, string
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

d = {
  "@": "a",
  "[": "c",
  "!": "i",
  ";": "j",
  "^": "n",
  "0": "o",
  "7": "t",
  "\\\\'": "w",
  "\\'": "v",
}


def solve():
  s = inp()

  total = 0
  cnt = 0

  i = 0
  while i < len(s):
    for k in d.keys():
      if s[i:len(k)+i] == k:
        cnt += 1
        i += len(k)
        total += 1
        break
    else:
      if 'a' <= s[i] <= 'z':
        total += 1
      i += 1

  if cnt * 2 >= total:
    return "I don't understand"

  for k, v in d.items():
    s = s.replace(k, v)
  
  return s

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(ret)
