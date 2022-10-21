"""
[8760: Schronisko](https://www.acmicpc.net/problem/8760)

Tier: Bronze 4
Category: 구현
"""


def solution():
  for _ in range(int(input())):
    a, b = map(int, input().split())

    l = []

    if a % 2 == 1:
      l.append((a - 1) * b // 2 + b // 2)

    if b % 2 == 1:
      l.append((b - 1) * a // 2 + a // 2)

    if a % 2 == 0 or b % 2 == 0:
      l.append(a * b // 2)

    print(max(l))


if __name__ == '__main__':
  solution()
