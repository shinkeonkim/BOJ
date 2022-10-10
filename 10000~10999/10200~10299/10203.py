"""
[10203: Count Vowels](https://www.acmicpc.net/problem/10203)

Tier: Bronze 2
Category: 구현
"""


def solution():
  for _ in range(int(input())):
    s = input()
    print(f'The number of vowels in {s} is {sum([s.count(c) for c in "aeiou"])}.')


if __name__ == '__main__':
  solution()
