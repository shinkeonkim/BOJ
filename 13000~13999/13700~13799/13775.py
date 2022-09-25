'''
[13775: Virus](https://www.acmicpc.net/problem/13775)

Tier: Bronze 2
Category: 구현
'''


def solution():
  key = int(input())
  s = input()

  for i in s:
    if 'a' <= i <= 'z':
      print(end=chr((ord(i) - 97 - key + 26) % 26 + 97))
      key += 1
      if key == 26:
        key = 1
    else:
      print(end=i)


if __name__ == '__main__':
  solution()
