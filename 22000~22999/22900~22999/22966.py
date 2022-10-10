"""
[22966: 가장 쉬운 문제를 찾는 문제](https://www.acmicpc.net/problem/22966)

Tier: Bronze 2
Category: 구현

print(sorted([input().split() for _ in range(int(input()))], key=lambda t: int(t[1]))[0][0])
"""


def solution():
  return sorted([input().split() for _ in range(int(input()))], key=lambda t: int(t[1]))[0][0]


if __name__ == '__main__':
  print(solution())
