'''
[19813: Dates](https://www.acmicpc.net/problem/19813)

Tier: Bronze 2
Category: 구현, 문자열
'''


def solution():
  for i in range(int(input())):
    s = input()
    if '.' in s:
      s = [*map(int, s.split('.'))]
    else:
      s = [*map(int, s.split('/'))]
      s[0], s[1] = s[1], s[0]

    print('%02d.%02d.%04d %02d/%02d/%04d' % (s[0], s[1], s[2], s[1], s[0], s[2]))


if __name__ == '__main__':
  solution()
