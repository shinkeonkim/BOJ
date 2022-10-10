"""
[6550: 부분 문자열](https://www.acmicpc.net/problem/6550)

Tier: Silver 5
Category: 문자열, 그리디 알고리즘
"""


def solution():
  while 1:
    try:
      s, t = input().split()
    except:
      break

    s_crt = 0  # crt는 current의 약어로 많이 사용됩니다.

    for tt in t:
      if tt == s[s_crt]:
        s_crt += 1

      if s_crt >= len(s):
        break

    print('Yes' if s_crt == len(s) else 'No')


if __name__ == '__main__':
  solution()
