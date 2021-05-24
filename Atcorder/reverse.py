# 入力された数字を反転させる
n = int(input())
lst = list(map(int, input().split()))
lst.reverse()

for i in lst:
    print(i, end=' ')

# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

n = input()
lst = list(map(int, input().split()))
result_lst = lst[::-1]
print(result_lst)  # [5, 4, 3, 2, 1]
print(*result_lst)  # 5 4 3 2 1
