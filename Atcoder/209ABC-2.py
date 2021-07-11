N, X = map(int, input().split())
Alst = list(map(int, input().split()))
# print(Alst) #[3, 3, 4, 4]
total = sum(Alst)
# print(total)  # 14

if N % 2 == 0:  # 偶数
    tmp = total - (N//2)
else:
    tmp = total - (N-1) // 2

if tmp <= X:
    print("Yes")
else:
    print("No")
