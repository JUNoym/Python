n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for j in range(m)]
# print(A)
# print(B)
C = [[0]*n for i in range(l)]
# print(C)

for x in range(n):
    for y in range(m):
        for z in range(l):
            C[x][z] += A[x][y] * B[y][z]


for row in range(n):
    print(*C[row])
