'''
[7366: Counting Shepp](https://www.acmicpc.net/problem/7366)

Tier: Bronze 2
Category: 문자열
'''


def solution():
  for tc in range(1, int(input()) + 1):
    input()
    print(f"Case {tc}: This list contains {input().split().count('sheep')} sheep.")
    print()


if __name__ == '__main__':
  solution()
