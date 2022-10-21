"""
[23055: 공사장 표지판](https://www.acmicpc.net/problem/23055)

Tier: Bronze 2
Category: 구현
"""


def solution(n):
  for i in range(n):
    for j in range(n):
      if i == 0 or j == 0 or i == n - 1 or j == n - 1 or i == j or i == n - j - 1:
        print(end='*')
      else:
        print(end=' ')
    print()


if __name__ == '__main__':
  solution(int(input()))
