from math import factorial

# print(factorial(10)) # 10!
# 順列の総数を算出

# def P_count(n, r):
#     return factorial(n) // factorial(n-r)

# print(P_count(4, 4))
# ----------------------------------
P = int(input())
coin = [1]
tmp = 1

for i in range(2, 11):
    tmp *= i
    coin.append(tmp)
print(coin)

ans = 0
for j in reversed(range(10)):
    ans += P // coin[j]
    P = P % coin[j]

print(ans)

# 動的計画法を用いる解放
P = int(input())
dp = [10 ** 9 for i in range(P+1)]
#dp[i] = i円支払うのに必要な硬貨の枚数の最小値
dp[0] = 0
fact = [1]
now = 1
for i in range(2, 11):
    now *= i
    fact.append(now)
print(fact)
for i in range(10):
    for j in range(1, P+1):
        if j >= fact[i]:
            dp[j] = min(dp[j], dp[j-fact[i]] + 1)
print(dp[P])

# 別解
P = int(input())
coinList = []
coinTmp = 1
for i in range(1, 11):
    coinTmp *= i
    coinList.append(coinTmp)
# print(coinList)

coinCount = 0

for i in range(9, -1, -1):
    if P >= coinList[i]:
        coinCount += P // coinList[i]
        P = P % coinList[i]


print(coinCount)
