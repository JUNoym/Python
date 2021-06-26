n, k = map(int, input().split())
ablst = [list(map(int, input().split())) for i in range(n)]
ablst.sort()

sumMoney = k

for i in range(n):
    if sumMoney >= ablst[i][0]:
        sumMoney += ablst[i][1]
print(sumMoney)
