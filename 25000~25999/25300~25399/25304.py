"""
[25304: 영수증](https://www.acmicpc.net/problem/25304)

Tier: Bronze 5
Category: 구현
"""


def solution():
  s = int(input())
  for _ in range(int(input())):
    a, b = map(int, input().split())
    s -= a * b

  return 'Yes' if s == 0 else 'No'


if __name__ == '__main__':
  print(solution())
