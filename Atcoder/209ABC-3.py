N = int(input())
Clst = list(map(int, input().split()))
Clst.sort()
# print(Clst)
ans = 1

for i in range(N):
    ans = ans * max(0, Clst[i] - i) % 1000000007
print(ans)
