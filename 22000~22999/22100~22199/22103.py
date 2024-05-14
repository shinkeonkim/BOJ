"""
[22103: Командная олимпиада](https://www.acmicpc.net/problem/22103)

Tier: Bronze 1
Category: 구현
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n, m, p, q, t = mii()
  
  # c1: 주인공이 푼 대화형 문제 개수
  
  ans = 1e12

  for c1 in range(0, t // p + 1):
    c2 = (t - c1 * p) // q    
    left_n = n - c1
    left_m = m - c2
    
    
    a = t // p
    b = t // q
    cnt = left_n // a + int(left_n % a > 0) + left_m // b + int(left_m % b > 0)
    
    ans = min(ans, cnt)
  
  print(ans + 1)


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
