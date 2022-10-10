"""
[14244: 트리 만들기](https://www.acmicpc.net/problem/14244)

Tier: Silver 4
Category: 트리, 스페셜 저지
"""


def solution(n, m):
  for i in range(m - 1):
    print(i, m - 1)

  for i in range(m - 1, n - 1):
    print(i, i + 1)


if __name__ == '__main__':
  n, m = map(int, input().split())
  solution(n, m)
