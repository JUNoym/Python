n = int(input())
a = list(map(int, input().split()))
rui = [0]*(n+1)
for i in range(1, n+1):
    rui[i] = rui[i-1]+a[i-1]
m = 0
cnt = 0
for i in range(n):
    m = max(a[i], m)
    cnt += rui[i+1]
    print(m*(i+1)+cnt)
