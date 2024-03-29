# 入力
N = int(input())

# 計算の舞台となる配列の定義
# 全体を 0 で初期化する
T = [0] * (N+1)

# 初期値の設定
T[0] = 1

# 順に計算していく
for i in range(1, N+1):
    if i-1 >= 0:
        T[i] += T[i-1]
    if i-2 >= 0:
        T[i] += T[i-2]
    if i-3 >= 0:
        T[i] += T[i-3]
print(T[N]) 