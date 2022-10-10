"""
[25594: HG 음성기호](https://www.acmicpc.net/problem/25594)

Tier: Silver 5
Category: 구현
"""


d = {
  'a': 'aespa',
  'b': 'baekjoon',
  'c': 'cau',
  'd': 'debug',
  'e': 'edge',
  'f': 'firefox',
  'g': 'golang',
  'h': 'haegang',
  'i': 'iu',
  'j': 'java',
  'k': 'kotlin',
  'l': 'lol',
  'm': 'mips',
  'n': 'null',
  'o': 'os',
  'p': 'python',
  'q': 'query',
  'r': 'roka',
  's': 'solvedac',
  't': 'tod',
  'u': 'unix',
  'v': 'virus',
  'w': 'whale',
  'x': 'xcode',
  'y': 'yahoo',
  'z': 'zebra',
}


def solution(s):
  idx = 0
  ans = ''

  while idx < len(s):
    word = d[s[idx]]
    if s[idx:idx + len(word)] == word:
      ans += s[idx]
      idx += len(word)
    else:
      return 'ERROR!'

  return f"It's HG!\n{ans}"


if __name__ == '__main__':
  print(solution(input()))
