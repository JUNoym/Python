N, X = map(int, input().split())

for i in range(2, N+1):
    if i % X == 0:
        print(i)
