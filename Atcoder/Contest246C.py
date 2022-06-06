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


# ACのコード
N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
rem = K  # クーポンの残り枚数
Q = sum(x // X for x in A)  # X円引きできる回数
R = sorted((x % X for x in A), reverse=True)  # X円引きし終わったあとの余りを大きい順に並べる
ans -= X * min(Q, rem)  # Qとクーポンの枚数の少ない方だけX円引きできる
rem -= min(Q, rem)  # X円引きに使った分クーポンを減らす
ans -= sum(R[:rem])  # 大きい順に使う（スライスは配列外参照を起こさないので、remが巨大でも問題ありません）
print(ans)