"""
[16165: 걸그룹 마스터 준석이](https://www.acmicpc.net/problem/16165)

Tier: Silver 3
Category: 구현
"""


def solution():
  n, m = map(int, input().split())
  team = {}
  member = {}

  for _ in range(n):
    team_name = input()
    member[team_name] = []
    k = int(input())
    for __ in range(k):
      name = input()
      member[team_name].append(name)
      team[name] = team_name

  for key in member:
    member[key] = sorted(member[key])

  for _ in range(m):
    s = input()
    q = int(input())
    if q == 0:
      print('\n'.join(member[s]))
    else:
      print(team[s])


if __name__ == '__main__':
  solution()
