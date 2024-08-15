"""
[19939: 박 터뜨리기](https://www.acmicpc.net/problem/19939)

Tier: Silver 4 
Category: greedy, math
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
  n, k = mii()
  
  # n개의 공을 k개의 바구니에 넣는다.
  # 각 바구니에는 최소 1개의 공이 있어야 한다.
  # 긱 바구니에 담긴 공의 개수는 모두 달라야 한다.
  # 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되어야 한다.
  
  z = k * (k + 1) // 2
  
  if n < z:
    # 1 부터 k까지의 합
    p(-1)
    return

  if n == z:
    p(k - 1)
    return
  

  if (n - z) % k == 0:
    p(k - 1)
    return

  p(k)
  
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()