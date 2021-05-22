N = int(input())
lst = []
count = 0

for i in range(N):
    a = list(map(int, input().split()))
    lst.append(a)
# print(lst)


A = (lst[0][0], lst[0][1], lst[0][2])
B = (lst[1][0], lst[1][1], lst[1][2])
C = (lst[2][0], lst[2][1], lst[2][2])
print(A)
print(B)
print(C)

for i in range(1, N+1):
    for j in range(1, N+1):
        bcj = C[j-1]
        if A[i-1] == B[bcj-1]:
            count += 1

print(count)
