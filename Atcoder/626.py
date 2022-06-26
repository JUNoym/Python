# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

# 再帰関数 (A の前から i 個の中からいくつか選んで j を作れるか)
def func(i, j):
    # i = 0 のとき、 j = 0 なら true
    if i==0:
        return j==0

    # それ以外のとき、問題文の通りに判定する
    flag = False
    if j>=A[i-1] and func(i-1, j-A[i-1]):
        flag = True
    if func(i-1, j):
        flag = True

    return flag

# 入力
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 出力
if func(N, X):
    ans = "Yes"
else:
    ans = "No"
print(ans)