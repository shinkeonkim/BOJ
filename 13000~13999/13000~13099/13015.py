"""
[13015: 별 찍기 - 23](https://www.acmicpc.net/problem/13015)

Tier: Silver 5
Category: 구현
"""


def solution():
  n = int(input())

  print('*' * n + ' ' * ((n - 2) * 2 + 1) + '*' * n)

  for i in range(1, n - 1):
    print(' ' * i + '*' + ' ' * (n - 2) + '*' + ' ' * ((n - 2 - i) * 2 + 1) + '*' + ' ' * (n - 2) + '*')

  print(' ' * (n - 1) + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*')

  for i in range(n - 2, 0, -1):
    print(' ' * i + '*' + ' ' * (n - 2) + '*' + ' ' * ((n - 2 - i) * 2 + 1) + '*' + ' ' * (n - 2) + '*')

  print('*' * n + ' ' * ((n - 2) * 2 + 1) + '*' * n)


if __name__ == '__main__':
  solution()
