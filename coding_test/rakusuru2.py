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
# リストに*を付けて関数の引数に指定すると、それぞれの要素が展開され個別の引数として渡される。
# print(*l)  # => print(0, 1, 2)
# 0 1 2
# print(*l, sep='')
# 012

# print(*l, sep='-')
# 0-1-2