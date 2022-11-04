"""
[15702: 중간고사 채점](https://www.acmicpc.net/problem/15702)

Tier: Silver 5
Category: 구현
"""


def solution():
  N, M = map(int, input().split())
  l = [*map(int, input().split())]
  D = [input().split() for _ in range(M)]
  scores = []

  for i in range(M):
    s = 0
    for j in range(N):
      if D[i][j + 1] == 'O':
        s += l[j]

    scores.append([int(D[i][0]), s])

  scores.sort(key=lambda s: (-s[1], s[0]))

  print(*scores[0])


if __name__ == '__main__':
  solution()
