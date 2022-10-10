"""
[25641: 균형 잡힌 소떡소떡](https://www.acmicpc.net/problem/25641)

Tier: Bronze 3
Category: 구현, 문자열
"""


def solution():
  input()  # n은 사용하지 않는다.

  s = input()[::-1]  # 문자열을 뒤집어, 뒤에서부터 순회하기 쉽게 만든다.

  ans = ''
  tmp = ''

  s_cnt, t_cnt = 0, 0

  for i in s:
    if i == 's':
      s_cnt += 1
    if i == 't':
      t_cnt += 1

    tmp += i

    # s와 t의 개수가 같을 때, ans에 저장한다.
    if s_cnt == t_cnt:
      ans = tmp

  # 뒤에서부터 순회했기 때문에 거꾸로 뒤집어 반환한다.
  return ans[::-1]


if __name__ == '__main__':
  print(solution())
