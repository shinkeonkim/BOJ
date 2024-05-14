"""
[3076: 상근이의 체스판](https://www.acmicpc.net/problem/3076)

Tier: Bronze 2
Category: 구현
"""


def solution():
  # R: 행의 수, C: 열의 수
  # A: 행의 높이, B: 열의 너비

  R, C = map(int, input().split())
  A, B = map(int, input().split())

  k = ['X', '.']

  for row in range(R):
    for _row2 in range(A):
      for column in range(C):
        for _column2 in range(B):
          print(k[(row + column) % 2], end='')
      print()


if __name__ == '__main__':
  solution()
