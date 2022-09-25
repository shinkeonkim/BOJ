'''
[6993: Shift Letters](https://www.acmicpc.net/problem/6993)

Tier: Bronze 2
Category: 문자열
'''


def solution():
  for _ in range(int(input())):
    s, cnt = input().split()
    cnt = int(cnt)

    print(f'Shifting {s} by {cnt} positions gives us: {s[-cnt:]+s[:-cnt]}')


if __name__ == '__main__':
  solution()
