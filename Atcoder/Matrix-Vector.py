N, M = map(int, input().split())

A = [[] for i in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

B = [[0]*1 for i in range(M)]

for i in range(M):
    B[i] = int(input())


for row in range(N):
    tmp = 0
    for col in range(M):
        tmp += A[row][col]*B[col]
    print("%d" % (tmp))
