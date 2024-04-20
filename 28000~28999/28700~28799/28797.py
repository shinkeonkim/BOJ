"""
[28797: Дневнегреческая машина](https://www.acmicpc.net/problem/28797)

Tier: Bronze 1
Category: 구현, 수학, (삼분탐색 / 끼얹기)

수식으로 해결될 것 같았는데, 잘 모르겠어서 값 넣어보면서
그래프가 최대값이 하나만 나오게 꼭짓점이 있는 형태였음. 그래서 삼분탐색으로 그래프 훑음..
이후에 푼 사람들 풀이를 보니 아래와 같이 해결됨.
if (x < 1):
  return x * 100
else:
  return ((x - 1) / 3 + 1) * 100
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

def f(A, dis):
  need = dis / 100
  
  mn = A - 3 * need
  
  if mn < 0:
    return 0
  
  mn = min(1, mn)
  
  return (need + mn) * 100

def solve():
  A = fi()
  
  if A <= 1:
    return A * 100
  
  left = 0
  right = 100
  ans = 100
  
  delta = 0.00000001

  while left <= right:
    lmid = left * 2 / 3 + right / 3
    rmid = left / 3 + right * 2 / 3
    
    x = f(A, lmid)
    y = f(A, rmid)
    
    if x > y:
      ans = max(ans, x)
      right = rmid - delta
    else:
      ans = max(ans, y)
      left = lmid + delta
    
  return ans


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
    p(ret)
