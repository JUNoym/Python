H,W = map(int, input().split())

lst = [input() for i in range(H)]
# print(lst)
# じゃあ二重ループでoを探してidx取得してそこから二つ目の座業引く一つ目の座標を計算すれば答えが出そう
idx1 = []
for i,v in enumerate(lst):
    for j,vv in enumerate(v):
        if vv == "o":
            idx1.append([i,j])

print((abs(idx1[1][0] - idx1[0][0]) + abs(idx1[1][1] - idx1[0][1])))