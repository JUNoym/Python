pattern = ["S", "H", "C", "D"]
check = [[False for i in range(13)] for j in range(4)]
n = int(input())

for i in range(n):
    e, num = input().split()
    num = int(num)
    check[pattern.index(e)][num-1] = True

print(check)

for i in range(4):  # 0123
    for j in range(13):  # 0 1 2 3 4 5 6 7 8 9 10 11 12
        if check[i][j] == False:
            print(pattern[i], j+1)
