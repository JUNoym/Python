r, c = map(int, input().split())  # 4 5
sheet = [list(map(int, input().split())) for i in range(r)]

for row in range(r):  # 0 1 2 3
    sheet[row].append(sum(sheet[row]))

col_sum = [0]*(c+1)  # [0 0 0 0 0 0]

for col in range(c+1):
    for row in range(r):
        col_sum[col] += sheet[row][col]

for row in range(r):
    print(*sheet[row])
print(*col_sum)

# input
# 4 ​5
# 1 1 3 4 5
# 2 2 2 4 5
# 3 3 0 1 1
# 2 3 4 4 6
