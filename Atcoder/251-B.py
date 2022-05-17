N,W = map(int, input().split())
Alst = list(map(int, input().split()))
can = [False]*(W+1)
# オモリを一個選んだ場合
for i in range(N):
    if Alst[i] <= W:
        can[Alst[i]] = True
 
# オモリを２個選んだ場合
for i in range(N): #01
    for j in range(i+1,N):
        s = Alst[i] + Alst[j]
        if s <= W:
            can[s] = True
 
# オモリを３個選んだ場合
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s = Alst[i] + Alst[j] + Alst[k]
            if s <= W:
                can[s] = True
 
ans = 0
for c in can:
    if c:
        ans += 1
 
print(ans)