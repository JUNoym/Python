pattern = ["S", "H", "C", "D"]
check = [[0 for i in range(13)] for j in range(4)]

n = int(input())

for i in range(n):
    egara, num = input().split()
    num = int(num)
    if check[pattern.index(egara)][num-1] == 0:
        check[pattern.index(egara)][num-1] = True


for j, row in enumerate(check):
    for i, v in enumerate(row):
        if v == 0:
            e = pattern[j]
            print(e, i+1)
