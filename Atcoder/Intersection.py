N = int(input())
Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))

res = 0
for x in range(1, 1001):
    Flag = True
    for y in range(N):
        if x < Alist[y] or x > Blist[y]:
            Flag = False
    if Flag:
        res += 1
print(res)
