result = 0
n, k = map(int, input().split())


table = [list(map(int, input().split())) for i in range(n)]
# print(table[4][1])

for row in range(n):
    if table[row][0] >= k:
        result += table[row][1]
print(result)

# 5 5000
# 100 6135
# 250 2935
# 1000 4890
# 5000 125
# 10000 1500
