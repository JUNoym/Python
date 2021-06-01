# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_7_B
while True:
    N, X = map(int, input().split())
    if N == 0:
        break
    res = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if i + j + k == X:
                    res += 1
    print(res)
