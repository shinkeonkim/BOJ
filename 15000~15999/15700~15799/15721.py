"""
[15721: 번데기](https://www.acmicpc.net/problem/15721)

Tier: Silver 5 
Category: bruteforcing, implementation, simulation

문제
중앙대학교 소프트웨어학부에 새로 입학한 19학번 새내기 일구는 새내기 새로 배움터에 가서 술게임을 여러 가지 배웠다. 그 중 가장 재미있었던 게임은 바로 번데기 게임이었다.

번데기 게임의 규칙은 다음과 같다. ‘뻔 – 데기 – 뻔 – 데기 – 뻔 – 뻔 – 데기 – 데기’ 를 1회차 문장이라고 하자. 2회차 문장은 ‘뻔 – 데기 – 뻔 - 데기 – 뻔 – 뻔 – 뻔 – 데기 – 데기 – 데기’가 된다. 즉 n-1회차 문장일 때는 ‘뻔 – 데기 – 뻔 – 데기 – 뻔(x n번) – 데기(x n번)’이 된다. 하이픈 사이를 지날 때마다 순서는 다음 사람으로 넘어간다. 원을 돌아 다시 일구 차례가 와도 게임은 계속 진행된다.

일구와 동기들, 그리고 선배들을 포함한 사람 A명이 다음과 같이 원으로 앉아 있다고 가정하자. 

일구가 0번째이고, 반 시계 방향으로 번데기 게임을 진행한다. T번째 ‘뻔’ 또는 ‘데기’를 외치는 사람은 위 원에서 몇 번 사람인지를 구하여라. (새내기는 10000번째가 되는 순간 시체방에 가기 때문에 T는 10000이하의 임의의 자연수이다.)

입력
첫째 줄에 게임을 진행하는 사람 A명이 주어진다. A는 2,000보다 작거나 같은 자연수이다.

둘째 줄에는 구하고자 하는 번째 T가 주어진다. (T ≤ 10000)

셋째 줄에는 구하고자 하는 구호가 “뻔”이면 0, “데기”면 1로 주어진다. 

출력
첫째 줄에 구하고자 하는 사람이 원탁에서 몇 번째에 있는지 정수로 출력한다. 

예제 입력 1 
8
2
0
예제 출력 1 
2

예제 입력 2 
4
6
1
예제 출력 2 
3
힌트
예를 들어 7명이 있고, 16번째 등장하는 “뻔”을 부른 사람의 번호를 알고 싶다면 입력은 7 16 0이다. 4명이 있고 6번째 등장하는 “데기”를 부른 사람의 번호를 알고 싶다면 입력은 4 6 1이며, 이때 출력 값은 반 시계 방향으로 3번째 있는 사람이므로 3을 출력한다. 
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
  A = ii()
  T = ii()
  
  flag = ii()
  
  cnt = 0
  total_cnt = 0
  
  local_cnt = 0
  i = 1
  
  뻔데기 = [0, 1, 0, 1]
  crt = 0
  
  while cnt < T:
    if local_cnt == 4 + 2 * (i + 1):
      local_cnt = 0
      i += 1
    
    if local_cnt < 4:
      crt = 뻔데기[local_cnt]
    else:
      if local_cnt < (i + 1) + 4:
        crt = 0
      else:
        crt = 1
    
    if crt == flag:
      cnt += 1
    
    total_cnt += 1
    local_cnt += 1
  
  return (total_cnt - 1) % A


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    
    p(ret)