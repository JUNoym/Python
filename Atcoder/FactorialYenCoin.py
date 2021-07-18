from math import factorial

P = int(input())
# print(factorial(10)) # 10!
# 順列の総数を算出

# def P_count(n, r):
#     return factorial(n) // factorial(n-r)

# print(P_count(4, 4))

coin = []
tmp = 1

for i in range(1, 11):
    tmp *= i
    coin.append(tmp)
print(coin)

ans = 0
for j in reversed(range(10)):
    ans += P // coin[j]
    P = P % coin[j]

print(ans)
