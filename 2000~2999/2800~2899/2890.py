n, m = map(int, input().split())

map_table = [input() for _ in range(n)]

team_places = {}

for i in range(n):
  for j in range(m - 1, -1, -1):
    if '1' <= map_table[i][j] <= '9':
      team_places[int(map_table[i][j])] = j
      break

team_places = sorted([*team_places.items()], key=lambda t: -t[1])

ans = {}

cnt = 1
ans[team_places[0][0]] = cnt
for idx in range(1, 9):
  if team_places[idx][1] != team_places[idx - 1][1]:
    cnt += 1
  ans[team_places[idx][0]] = cnt

ans = sorted([*ans.items()], key=lambda t: t[0])

print(*map(lambda a: a[1], ans), sep='\n')
