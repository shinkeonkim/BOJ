"""
[24510: 시간복잡도를 배운 도도](https://www.acmicpc.net/problem/24510)

Tier: Bronze 2
Category: 구현
"""


def solution():
  ans = 0

  for _ in range(int(input())):
    s = input()
    ans = max(ans, s.count('for') + s.count('while'))

  return ans


if __name__ == '__main__':
  print(solution())
