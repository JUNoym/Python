r, c = map(int, input().split())  # 4 5
sheet = [list(map(int, input().split())) for i in range(r)]
for i in range(r):  # 0 1 2 3
    sheet[i].append(sum(sheet[i]))
    print(sheet[i])
Column_sum = [0]*(c+1)
for j in range(c+1):  # 0 1 2 3 4 5
    for i in range(r):  # 0 1 2 3
        Column_sum[j] += sheet[i][j]

for i in range(r):
    print(*sheet[i])
print(*Column_sum)
