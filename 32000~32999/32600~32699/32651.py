"""
[32651: 인간은 무엇인가](https://www.acmicpc.net/problem/32651)

Tier: Bronze 4 
Category: arithmetic, implementation, math
"""


n = int(input())
print("Yes" if n % 2024 == 0 and n <= 100000 else "No")