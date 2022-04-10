# N × N の二次元配列を左向きに90°回転させるメソッドを書く
# 入力: N
# 出力: N × N の二次元配列

N = int(input())
data = [input() for _ in range(N)]
ans = [[''] * N for _ in range(N)]
print(data)

for i in range(N):
    for j in range(N):
        ans[j][i] = data[i][j]
for x in ans:
    print(*x,sep='')