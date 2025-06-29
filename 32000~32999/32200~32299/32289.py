"""
[32289: Max-Queen](https://www.acmicpc.net/problem/32289)

Tier: Silver 5 
Category: greedy, math
"""


n, m = map(int, input().split())
print(2 * (n - 1) * (m - 1) + n * (m - 1) + m * (n - 1))
