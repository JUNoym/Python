N, K = map(int, input().split())
alist = list(map(int, input().split()))
tmp = K // N  # 3
K = K % N  # 1
ans = [tmp for _ in range(N)]  # 0 1
print(ans)

order = []

for i in range(N):
    order.append([alist[i], i])
print(order)

order.sort()
print(order)

for i in range(K):
    ans[order[i][1]] += 1

for a in ans:
    print(a)
