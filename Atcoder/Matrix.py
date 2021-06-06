
N, M, L = map(int, input().split())  # 3 2 3

A = [list(map(int, input().split())) for i in range(N)]  # N*M配列の取得
B = [list(map(int, input().split())) for i in range(M)]  # M*L配列の取得
ANS = [[0]*L for i in range(N)]  # N*L


for x in range(N):  # 0 1 2
    for y in range(L):  # 0 1 2
        for z in range(M):  # 0 1
            ANS[x][y] += B[z][y]*A[x][z]

for row in range(N):
    print("%d" % ANS[row][0], end="")
    for col in range(1, L):
        print(" %d" % (ANS[row][col]), end="")
    print()


# input
# 3 2 3
# 1 2
# 0 3
# 4 5
# 1 2 1
# 0 3 2
