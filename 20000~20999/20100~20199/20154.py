"""
[20154: 이 구역의 승자는 누구야?!](https://www.acmicpc.net/problem[20154)

Tier: Bronze 1
Category: 구현
"""


d = {
  'A': 3,
  'B': 2,
  'C': 1,
  'D': 2,
  'E': 3,
  'F': 3,
  'G': 3,
  'H': 3,
  'I': 1,
  'J': 1,
  'K': 3,
  'L': 1,
  'M': 3,
  'N': 3,
  'O': 1,
  'P': 2,
  'Q': 2,
  'R': 2,
  'S': 1,
  'T': 2,
  'U': 1,
  'V': 1,
  'W': 2,
  'X': 2,
  'Y': 2,
  'Z': 1,
}


def solution():
  s = input()
  l = [d[i] for i in s]

  while len(l) > 1:
    l2 = []

    for i in range(0, len(l), 2):
      if i + 1 >= len(l):
        l2.append(l[i])
      else:
        l2.append((l[i] + l[i + 1]) % 10)

    l = l2

  return "I'm a winner!" if l[0] % 2 else "You're the winner?"


if __name__ == '__main__':
  print(solution())
