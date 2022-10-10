"""
[23827: 수열 (Easy)](https://www.acmicpc.net/problem/23827)

Tier: Silver 4
Category: 구현
"""


def solution():
  input()
  numbers = [*map(int, input().split())]

  ans = 0
  sm = sum(numbers)

  for number in numbers:
    ans += number * (sm - number)

  ans //= 2
  ans %= 1000000007
  return ans


if __name__ == '__main__':
  print(solution())
