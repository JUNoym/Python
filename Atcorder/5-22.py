import sys
from collections import defaultdict
N = int(input())
count = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


for i in range(1, N+1):
    for j in range(1, N+1):
        bcj = C[j-1]
        if A[i-1] == B[bcj-1]:
            count += 1

print(count)


# [解答]
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
cnt = defaultdict(lambda: 0)
for i in a:
    cnt[i] += 1
ans = 0
for i in c:
    ans += cnt[b[i - 1]]
print(ans)
