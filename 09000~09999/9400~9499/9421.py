"""
[9421: 소수상근수](https://www.acmicpc.net/problem/9421)

Tier: Silver 1 
Category: math, number_theory, primality_test, sieve
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

def f(k):
  ret = 0
  while k > 0:
    ret += (k % 10) ** 2
    k //= 10
  return ret


def solve():
  # 1. 소수를 구한다.
  # 2. 소수 중에서도 자릿수마다 분리하여 제곱한 수를 더하는 과정을 무한 반복했을 떄 1로 끝나는 수를 구한다.

  n = ii() # 1 ~ n까지 수에 대해 구한다.

  # 소수 구하기

  primes = []
  is_prime = [True] * 10_000_000

  is_prime[0] = is_prime[1] = False

  for i in range(2, n + 1):
    if is_prime[i]:
      primes.append(i)
      for j in range(i * i, n + 1, i):
        is_prime[j] = False

  # 소수 중에서도 자릿수마다 분리하여 제곱한 수를 더하는 과정을 무한 반복했을 떄 1로 끝나는 수를 구한다.

  # 만약 1로 귀결되는 상황이면, 그 과정에 있던 모든 소수는 모두 소수상근수이다.
  # 만약 1로 귀결되지 않고 반복되는 상황이면, 그 과정에 있는 소수는 모두 소수상근수가 아니다.

  # visited를 0으로 채워놓고 시작
  # visisted에서 임시로 3을 채워놓고 결과에 따라 
  # 1로 귀결되었으면 3을 채워놓은 것을 1로 바꾼다.
  # 1로 귀결되지 않았으면 3을 채워놓은 것을 2로 바꾼다.

  ans = set()
  visited = [0] * 10_000_000

  for p in primes:
    visiting = []

    if visited[p] == 1:
      ans.add(p)
      continue
      
    if visited[p] == 2:
      continue

    visiting.append(p)
    visited[p] = 3

    ret = -1
    current = p

    while ret == -1:
      current = f(current)

      if visited[current] == 1 or current == 1:
        ret = 1
        break

      if visited[current] == 2:
        ret = 2
        break

      if visited[current] == 3:
        ret = 2
        break

      if visited[current] == 0:
        visiting.append(current)
        visited[current] = 3
    
    for v in visiting:
      visited[v] = ret
    
  for p in primes:
    if visited[p] == 1:
      ans.add(p)
  

  ans = sorted(list(ans))

  print(*ans, sep="\n")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()