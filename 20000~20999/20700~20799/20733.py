"""
[20733: Triple Texting](https://www.acmicpc.net/problem/20733)

Tier: Bronze 2
Category: 구현
"""


def solution():
  s = input()
  n = len(s) // 3

  for i in range(n):
    tmp = sorted([s[i], s[n + i], s[2 * n + i]])
    print(tmp[0] if tmp[0] == tmp[1] else tmp[1], end='')


if __name__ == '__main__':
  solution()
