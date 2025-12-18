"""
[9843: LVM](https://www.acmicpc.net/problem/9843)

Tier: Silver 4 
Category: implementation, data_structures, simulation, stack
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


def solve():
  stack = []
  register = 0
  commands = []
  
  for _ in range(ii()):
    commands.append(isplit())
    
  command_index = 0
  while 1:
    command = commands[command_index]
    # print(command, stack, register)
    
    if command[0] == 'PUSH':
      stack.append(int(command[1]))
      command_index += 1
      continue
    
    if command[0] == 'STORE':
      register = stack.pop()
      command_index += 1
      continue
    
    if command[0] == 'LOAD':
      stack.append(register)
      command_index += 1
      continue
    
    if command[0] == 'PLUS':
      a = stack.pop()
      b = stack.pop()
      stack.append(a + b)
      command_index += 1
      continue
  
    if command[0] == 'TIMES':
      a = stack.pop()
      b = stack.pop()
      stack.append(a * b)
      command_index += 1
      continue
    
    if command[0] == 'IFZERO':
      a = stack.pop()
      if a == 0:
        command_index = int(command[1])
      else:
        command_index += 1
      continue
    
    if command[0] == 'DONE':
      print(stack.pop())
      break


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
