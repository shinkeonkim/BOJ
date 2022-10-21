"""
[4583: 거울상](https://www.acmicpc.net/problem/4583)

Tier: Bronze 2
Category: 구현
"""


def solution():
  d = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',
    'i': 'i',
    'o': 'o',
    'v': 'v',
    'w': 'w',
    'x': 'x'
  }

  while 1:
    s = input()

    if s == '#':
      break

    ret = ''
    keys = d.keys()
    for i in s:
      if i not in keys:
        print('INVALID')
        break

      ret += d[i]
    else:
      print(ret[::-1])


if __name__ == '__main__':
  solution()
