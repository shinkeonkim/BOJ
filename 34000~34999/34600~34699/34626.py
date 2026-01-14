"""
[34626: Increase or Smash](https://www.acmicpc.net/problem/34626)

Tier: Silver 5
Category: greedy, ad_hoc
"""

for _ in range(int(input())):
  input()
  k = len(set([*map(int, input().split())]))
  print((k-1)*2+1)
