"""
[25704: 포인터 공부](https://www.acmicpc.net/problem/25704)

Tier: Bronze 5
Category: 구현
"""


def solution():
  n = int(input())

  print('int a;\nint *ptr = &a;')

  for i in range(2, n + 1):
    print(f'int {"*" * i}ptr{i} = &ptr{i - 1 if i > 2 else ""};')

  return ''


if __name__ == '__main__':
  solution()
