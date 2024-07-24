"""
[32089: 部員の変遷](https://www.acmicpc.net/problem/32089)

Tier: Bronze 4 
Category: implementation

春は別れと出会いの季節．今年もまた，伝統ある芸楽部の歴史に新たな名前を刻むときが来た．

部活日誌には，この部活の n 年分の部員の推移が記録されている．記録によれば，初年度より前の部員数はもちろん 0 人であり，毎年部員は 4 月に新入生のみが入部しており，3 年後の 3 月に卒業するタイミングでのみ退部しているようだ．

部の変遷を紐解くために，n 年間の各年の新入部員の数のデータから在籍する部員の数が最大になった年度の部員数を調べてみよう．

입력
入力は複数のデータセットからなる．データセットの個数は 50 を超えない．各データセットは次の形式で表される．

n a1 a2 … an

n は新入部員の数が記録されている年数を表す，3 以上 1000 以下の整数である．続く行は各年度の新入部員の数を表す n 個の整数からなり，i 年目の新入部員の数 ai はそれぞれ 0 ≤ ai ≤ 108 を満たす．

入力の終わりは，ゼロ 1 つだけからなる行で表される．

출력
各データセットについて，在籍する部員の数が最大になった年度の部員数を 1 行に出力せよ．
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

    a = mii()
    mx = 0
    cur = 0
    for i in range(n):      
      if i > 2:
        cur -= a[i-3]
      cur += a[i]
      mx = max(mx, cur)
      
    p(mx)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()