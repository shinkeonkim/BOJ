"""
[5738: He is offside!](https://www.acmicpc.net/problem/5738)

Tier: Bronze 1 
Category: implementation, sorting

문제
Hemisphere Network is the largest television network in Tumbolia, a small country located east of South America (or south of East America). The most popular sport in Tumbolia, unsurprisingly, is soccer; many games are broadcast every week in Tumbolia.

Hemisphere Network receives many requests to replay dubious plays; usually, these happen when a player is deemed to be offside by the referee. An attacking player is offside if he is nearer to his opponents’ goal line than the second last opponent. A player is not offside if

he is level with the second last opponent or
he is level with the last two opponents.
Through the use of computer graphics technology, Hemisphere Network can take an image of the field and determine the distances of the players to the defending team’s goal line, but they still need a program that, given these distances, decides whether a player is offside.

입력
The input file contains several test cases. The first line of each test case contains two integers A and D separated by a single space indicating, respectively, the number of attacking and defending players involved in the play (2 ≤ A, D ≤ 11). The next line contains A integers Bi separated by single spaces, indicating the distances of the attacking players to the goal line (1 ≤ Bi ≤ 104). The next line contains D integers Cj separated by single spaces, indicating the distances of the defending players to the goal line (1 ≤ Cj ≤ 104).

The end of input is indicated by a line containing only two zeros, separated by a single space.

The input must be read from standard input.

출력
For each test case in the input print a line containing a single character: “Y” (uppercase) if there is an attacking player offside, and “N” (uppercase) otherwise.

The output must be written to standard output.
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
  while 1:
    A, D = mii()
    
    if A == D == 0:
      break
    
    B = mii()
    C = mii()
    
    B.sort()
    C.sort()
    
    if B[0] < C[1]:
      p("Y")
    else:
      p("N")
    
  
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()