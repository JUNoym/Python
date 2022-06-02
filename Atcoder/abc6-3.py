n,a,b = map(int, input().split())
ans = [["o" for _ in range(n*b)] for _ in range(n*a)]

for i in range(n*a):
    for j in range(n*b):
        r = i//a
        c = j//b
   
        if (r+c)%2 == 0:
            ans[i][j]="."
        else:
            ans[i][j]="#"


for a in ans:
    # print(*a)
    print("".join(a))
