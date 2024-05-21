"""
[3088: 화분 부수기](https://www.acmicpc.net/problem/3088)

Tier: Silver 2
Category: 구현
"""

D = [False] * 1100000


def solution():
  l = [[*map(int, input().split())] for _ in range(int(input()))]

  cnt = 1

  for i in range(3):
    D[l[0][i]] = True

  for i in range(1, len(l)):
    chk = False
    for j in range(3):
      if D[l[i][j]]:
        chk = True

    if not chk:
      cnt += 1

    for j in range(3):
      D[l[i][j]] = True

  return cnt


if __name__ == '__main__':
  print(solution())
