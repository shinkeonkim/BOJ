"""
[9733: 꿀벌](https://www.acmicpc.net/problem/9733)

Tier: Silver 5
Category: 구현
"""


def solution():
  counter = {
    'Re': 0,
    'Pt': 0,
    'Cc': 0,
    'Ea': 0,
    'Tb': 0,
    'Cm': 0,
    'Ex': 0,
  }
  cnt = 0

  while True:
    try:
      a = input()
    except:
      break

    words = a.split()
    cnt += len(words)

    for word in words:
      if word in counter:
        counter[word] += 1

  for key in counter:
    print('%s %d %.2f' % (key, counter[key], counter[key] / cnt))

  print('Total %d 1.00' % (cnt))


if __name__ == '__main__':
  solution()
