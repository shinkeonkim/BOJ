"""
[20205: 교수님 그림이 깨지는데요?](https://www.acmicpc.net/problem/20205)

Tier: Bronze 1
Category: 구현
"""


def solution():
  n, k = map(int, input().split())

  l = [[*map(int, input().split())] for i in range(n)]

  for y in range(n):
    for y_k in range(k):
      for x in range(n):
        for x_k in range(k):
          print(l[y][x], end=' ')
      print()


if __name__ == '__main__':
  solution()
