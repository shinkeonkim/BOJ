"""
[6511: Black and white painting](https://www.acmicpc.net/problem/6511)

Tier: Bronze 2 
Category: arithmetic, math
Black and white painting 다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	80	46	42	56.757%
문제
You are visiting the Centre Pompidou which contains a lot of modern paintings. In particular you notice one painting which consists solely of black and white squares, arranged in rows and columns like in a chess board (no two adjacent squares have the same colour). By the way, the artist did not use the tool of problem A to create the painting.

Since you are bored, you wonder how many 8 × 8 chess boards are embedded within this painting. The bottom right corner of a chess board must always be white.

입력
The input contains several test cases. Each test case consists of one line with three integers n, m and c. (8 ≤ n, m ≤ 40000), where n is the number of rows of the painting, and m is the number of columns of the painting. c is always 0 or 1, where 0 indicates that the bottom right corner of the painting is black, and 1 indicates that this corner is white.

The last test case is followed by a line containing three zeros.

출력
For each test case, print the number of chess boards embedded within the given painting.

예제 입력 1 
8 8 0
8 8 1
9 9 1
40000 39999 0
0 0 0
예제 출력 1 
0
1
2
799700028
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

def f(n, m, c):
  if n < 8 or m < 8:
    return 0
  n8 = n - 7
  m8 = m - 7
    
  if c == 1:
    return ((n8 + 1) // 2) * ((m8 + 1) // 2) + (n8 // 2) * (m8 // 2)
  return ((n8 + 1) // 2) * (m8 // 2) + (n8 // 2) * ((m8 + 1) // 2)

def solve():
  while 1:
    n, m, c = mii()
    
    if n == m == c == 0:
      break
    
    p(f(n, m, c))
    

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()