A, B, C, D, E, F, X= map(int, input().split())
takahasi = 0
aoki = 0
#高橋くんが何メートル進んだかを計算する
p = X // (A + C) #何回歩きと休憩を繰り返すのかを求める
remainder = X % (A + C) # あまりの秒数と歩きの秒数を比較する必要して、歩きの範囲で終わっているのか、休憩している範囲で終わっているのかを判定して、数値を計算する必要がある
s = p * A
if remainder <= A:
    s += remainder
else:
    s += A
takahasi = s*B

# 青木くんが何メートル進んだのかを計算する
p = X // (D + F)
remainder = X % (D + F)
s = p * D
if remainder <= A:
    s += remainder
else:
    s += A
aoki = s * E

if takahasi > aoki:
    print("Takahashi")
elif takahasi < aoki:
    print("Aoki")
elif takahasi == aoki:
    print("Draw")