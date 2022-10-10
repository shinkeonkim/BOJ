"""
[25629: 홀짝 수열](https://www.acmicpc.net/problem/25629)

Tier: Bronze 3
Category: 구현
"""


def solution():
  input()
  l = [*map(lambda t: int(t) % 2, input().split())]
  a, b = l.count(0), l.count(1)
  return int(a == b or a + 1 == b)


if __name__ == '__main__':
  print(solution())
