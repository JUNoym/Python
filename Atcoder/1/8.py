# 二次元平面上に N 個の点があります。i 個目の点の座標は (x i , y i ) です。
# この中から 2 個の点を選ぶとき、それらを結ぶ線分の長さの最大値を求めてください
# B問題

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


T = []
for i in range(N):
    for j in range(i + 1, N):
        T.append((distance(XY[i], XY[j])))
print(max(T))
