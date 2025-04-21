"""
[4289: Rock-Paper-Scissors Tournament](https://www.acmicpc.net/problem/4289)

Tier: Bronze 1 
Category: arbitrary_precision, arithmetic, implementation, math
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
    s = inp()

    if s == '0':
      break

    n, k = map(int, s.split())

    win = [0] * (n + 1)
    total = [0] * (n + 1)

    d = { "rock": 0, "paper": 1, "scissors": 2 }

    for _ in range(k * n * (n - 1) // 2):
      game = inp().split()
  
      player_1 = int(game[0])
      game[1] = d[game[1]]
      player_2 = int(game[2])
      game[3] = d[game[3]]

      if game[1] == game[3]:
        continue

      total[player_1] += 1
      total[player_2] += 1

      if (game[3] + 1) % 3 == game[1]:
        win[player_1] += 1
      else:
        win[player_2] += 1
    
    for i in range(1, n + 1):
      if total[i] == 0:
        print("-")
      else:
        print(f"{win[i] / total[i]:.3f}")
    print()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()