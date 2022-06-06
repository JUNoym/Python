N = int(input())
A = list(map(int, input().split()))
A[0] = 0
A[1] = A[1]

for i in range(2,N):
    a = A[i] + A[i-1]
    b = A[i-2] + (2*A[i])
    A[i] = min(a,b)
print(A[-1])