'''
[6783: English  or Frensh?](https://www.acmicpc.net/problem/6783)

Tier: Bronze 2
Category: 문자열
'''


def solution():
  t_count = 0
  s_count = 0

  for _ in range(int(input())):
    sentence = input().lower()

    t_count += sentence.count('t')
    s_count += sentence.count('s')

  if t_count > s_count:
    return 'English'

  return 'French'


if __name__ == '__main__':
  print(solution())
