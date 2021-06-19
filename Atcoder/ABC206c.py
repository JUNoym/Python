import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = 0

# Ai = [int(i) for i in range(N)]
# print(Ai)

for i in range(N):
    for j in range(i+1, N):
        if A[i] != A[j]:
            count += 1
print(count)
