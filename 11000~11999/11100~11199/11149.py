'''
[11149: Decode the Message](https://www.acmicpc.net/problem/11149)

Tier: Bronze 1
Category: 구현, 문자열
'''


def solution():
  for _ in range(int(input())):
    l = input().split()

    for i in l:
      s = sum([ord(j) - 97 for j in i]) % 27

      if s == 26:
        print(end=' ')
      else:
        print(end=chr(s + 97))
    print()


if __name__ == '__main__':
  solution()
