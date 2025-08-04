n=int(input())
print(2*n/sum(1 for i in [input().split() for _ in range(n)] if i[0][:2]!=i[2][:2]))
