r, c = map(int, input().split())
sheet = [list(map(int, input().split())) for i in range(r)]

for row in range(r):
    sheet[row].append(sum(sheet[row]))

col_sum = [0]*(c+1)

for col in range(c+1):
    for row in range(r):
        col_sum[col] += sheet[row][col]

for row in range(r):
    print(*sheet[row])
print(*col_sum)
