# Official House
n = int(input())
houses = [[[0 for r in range(10)]for f in range(3)] for b in range(4)]

for i in range(n):
    b, f, r, v = [int(x) for x in input().split()]
    houses[b-1][f-1][r-1] += v

for b in range(4):
    for f in houses[b]:
        print(" "+" ".join([str(x) for x in f]))
    if b != 3:
        print("####################")

# Matrix Vector

n, m = [int(x) for x in input().split()]
A = [[] for i in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

B = [0 for i in range(m)]
for i in range(m):
    B[i] = int(input())

for row in range(n):
    tmp = 0
    for col in range(m):
        tmp += A[row][col]*B[col]
    print(tmp)

# ----------------------------------------------
