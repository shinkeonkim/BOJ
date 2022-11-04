"""
[25643: 문자열 탑 쌓기](https://www.acmicpc.net/problem/25643)

Tier: Bronze 1
Category: 구현
"""


def solution():
  n, m = map(int, input().split())

  l = [input() for _ in range(n)]

  for i in range(1, n):
    prev = l[i - 1]
    crt = l[i]

    for j in range(1, m + 1):
      if prev[:j] == crt[-j:]:
        break

      if prev[-j:] == crt[:j]:
        break
    else:
      return 0

  return 1


if __name__ == '__main__':
  print(solution())
