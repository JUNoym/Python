Alist = list(map(int, input().split()))
Alist.sort()

ans = "No"
if Alist[1] - Alist[0] == Alist[2] - Alist[1]:
    ans = 'Yes'
print(ans)
