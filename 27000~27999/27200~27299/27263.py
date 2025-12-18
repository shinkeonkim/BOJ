"""
[27263: Древний английский](https://www.acmicpc.net/problem/27263)

Tier: Bronze 1 
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

	# •	단어의 처음이 아니고, 뒤에 h가 오지 않는 모든 s는 th로 바꾼다.
	# •	연속된 o가 두 개 이상 나올 경우, 처음 두 개의 o만 ou로 바꾼다. (예: ooo는 ouo가 됨)
def solve():
  s = inp()

  if s.startswith('e'):
    s = 'ae' + s[1:]
  
  if s.startswith('E'):
    s = 'Ae' + s[1:]

  idxs = []
  for i in range(1, len(s)):
    if s[i] == 's' and (i == len(s) - 1 or s[i + 1] != 'h'):
      idxs.append(i)

  if idxs:
    s2 = ""
    for i in range(len(idxs)):
      if i == 0:
        s2 += s[:idxs[i]] + 'th'
      else:
        s2 += s[idxs[i - 1] + 1:idxs[i]] + 'th'
    
    s2 += s[idxs[-1] + 1:]

    s = s2

  cnt = 0
  start = -1
  s = list(s)
  for i in range(len(s)):
    if s[i] == 'o' or s[i] == 'O':
      if start == -1:
        start = i
      cnt += 1
    else:
      if cnt >= 2:
        s[start + 1] = 'u'
      cnt = 0
      start = -1
  
  if cnt >= 2:
    s[start + 1] = 'u'
  
  print(''.join(s))


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
