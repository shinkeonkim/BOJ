"""
[21756: 지우개](https://www.acmicpc.net/problem/21756)

Tier: Bronze 2
Category: 구현
"""


def solution(n):
  numbers = [i + 1 for i in range(n)]

  while len(numbers) > 1:
    numbers = numbers[1::2]

  return numbers[0]


if __name__ == '__main__':
  print(solution(int(input())))
