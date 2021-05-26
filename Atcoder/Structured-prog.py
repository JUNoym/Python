# N以下の自然数のうち３の倍数もしくは３がつくものを小さい順に出力する
N = int(input())
for i in range(1, N+1):
    if i % 3 == 0 or "3" in str(i):
        print(f'{i}', end=' ')
print()
