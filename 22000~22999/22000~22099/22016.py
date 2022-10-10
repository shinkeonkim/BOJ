"""
[22016: 巻物 (Scroll) ](https://www.acmicpc.net/problem/22016)

Tier: Bronze 2
Category: 구현
"""


def solution():
  n, k = map(int, input().split())
  s = input()

  ans = s[:k - 1]
  for i in range(k - 1, n):
    ans += s[i].lower() if s[i].upper() == s[i] else s[i].upper()

  return ans


if __name__ == '__main__':
  print(solution())
