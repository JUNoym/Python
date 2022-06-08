N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
ans2 = 0

for i,v in enumerate(A):
    for j, vv in enumerate(B):
        if v == vv and i == j:
            ans += 1
        elif v == vv and i != j:
            ans2 += 1
print(ans)
print(ans2)
