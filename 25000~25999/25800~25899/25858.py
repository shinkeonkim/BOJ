"""
[25858: Divide the Cash](https://www.acmicpc.net/problem/25858)

Tier: Bronze 4
Category: 구현
"""


def solution():
  n, d = map(int, input().split())
  l = [int(input()) for _ in range(n)]
  d = d // sum(l)

  for i in l:
    print(i * d)


if __name__ == '__main__':
  solution()
