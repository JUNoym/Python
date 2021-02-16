V, T, S, D = map(int, input().split())
if V*T <= D and D <= V*S:
    print('No')
else:
    print('Yes')

# -----------------------

N, X = map(int, input().split())
lst = list(map(int, input().split()))

ans = []
for i in lst:
    if i == X:
        continue
    ans.append(i)

print(*ans)　  # 可変長引数 複数の引数をタプルとして受け取ることができる
