"""
[33909: 알파벳 블록](https://www.acmicpc.net/problem/33909)

Tier: Bronze 3 
Category: math, implementation, arithmetic
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
  # SCON
  # S=N 상호 치환
  # O = 2 * C

  S, C, O, N = mii()

  A = S + N
  B = C + 2 * O

  # SCON = 2개의 a, 3개의 b , SCCC 1개의 a, 3개의 b

  ans = 0

  for i in range(A + 1):
    # SCCC
    sccc_count = i
    need_b = 3 * sccc_count

    if need_b > B:
      continue
    
    _A = A - sccc_count
    _B = B - need_b

    # SCON
    scon_count = min(_A // 2, _B // 3)

    # print(i, scon_count, sccc_count)

    ans = max(ans, min(scon_count, sccc_count))
    
  print(ans)
    

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()