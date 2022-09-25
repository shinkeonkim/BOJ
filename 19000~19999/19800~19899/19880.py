'''
[19880: Номер страницы](https://www.acmicpc.net/problem/19880)

Tier: Bronze 2
Category: 구현, 문자열
'''


def solution(s):
  n = len(s)
  ans = 0
  if s[0] == '0':
    return 0

  for i in range(1, n // 2 + 1):
    if s[i] == '0':
      continue

    if i + i < n:
      ans += 1
      continue

    if i == n - i and s[:i] <= s[i:]:
      ans += 1

  return ans


if __name__ == '__main__':
  print(solution(input()))
