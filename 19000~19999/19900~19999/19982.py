'''
[19982: ](https://www.acmicpc.net/problem/19982)

Tier: Bronze 2
Category: 구현
'''


def solution():
  n = int(input())
  a, b, c = map(int, input().split())

  ans = ''

  for i in range(a):
    ans += chr(65 + i % 26)

  for i in range(b):
    ans += chr(97 + i % 26)

  for i in range(n - (a + b)):
    ans += chr(48 + i % 10)

  return ans


if __name__ == '__main__':
  print(solution())
