"""
[22098: Треугольники](https://www.acmicpc.net/problem/22098)

Tier: Bronze 2
Category: 구현
"""


def f(a, b, c):
  if a + b <= c:
    return 3

  if c * c == a * a + b * b:
    return 0

  if c * c < a * a + b * b:
    return 1

  return 2


def solution():
  for _ in range(int(input())):
    l = sorted([*map(int, input().split())])
    d = [0, 0, 0, 0]

    for i in range(4):
      for j in range(i + 1, 4):
        for k in range(j + 1, 4):
          d[f(l[i], l[j], l[k])] += 1
    print(*d[:3])


if __name__ == '__main__':
  solution()
