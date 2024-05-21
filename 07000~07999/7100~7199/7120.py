'''
[7120: String](https://www.acmicpc.net/problem/7120)

Tier: Bronze 2
Category: 문자열
'''


def solution():
  sentence = input()
  ret = sentence[0]
  for c in sentence[1:]:
    if c == ret[-1]:
      continue
    ret += c

  return ret


if __name__ == '__main__':
  print(solution())
