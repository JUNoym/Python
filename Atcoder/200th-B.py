# https://atcoder.jp/contests/abc200/tasks/abc200_b
import math
N, K = map(int, input().split())

for i in range(K):
    N = int(N)
    if N % 200 == 0:
        N = N / 200
    else:
        N = str(N)
        N = N + "200"
        N = int(N)
print(math.floor(N))

# 解答
N, K = map(int, input().split())
for i in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = int(str(N) + '200')
print(N)
