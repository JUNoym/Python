from telnetlib import TELNET_PORT


# TLEのコード
N,K,X = map(int, input().split())
A = list(map(int, input().split()))
a = sorted(A, reverse=True)
# print(A)
# print(a)
for i in range(K):
    for j in range(N):
        while a[j] >= X:
            a[j] -= X
            K -= 1
# print(a) # ここでX以上の品物の値引きはできた配列が取得できる
# X円以下の品物から値引きを行なっていく
underX = sorted(a, reverse=True)
# print(underX)

for i in range(K):
    underX[i] -= X
    if underX[i] <= 0:
        underX[i] = 0
# print(underX)
print(sum(underX))
