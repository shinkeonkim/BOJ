"""
[5747: Odd or Even](https://www.acmicpc.net/problem/5747)

Tier: Silver 5 
Category: greedy
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

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
  while True:
    n = ii()
    if n == 0:
      break

    Xi = list(map(int, input().split()))
    Yi = list(map(int, input().split()))
    
    even_X = sum(1 for x in Xi if x % 2 == 0)
    odd_X = n - even_X
    even_Y = sum(1 for y in Yi if y % 2 == 0)
    odd_Y = n - even_Y
    
    john_wins = 0
    john_wins += min(even_X, odd_Y)
    john_wins += min(odd_X, even_Y)
    
    mary_wins = n - john_wins 
    
    print(mary_wins)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()