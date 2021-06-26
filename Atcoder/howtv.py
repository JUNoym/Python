from collections import Counter
S = list(map(str, input()))  # fcqdpfvcgb
A = list(map(str, input()))
B = list(map(str, input()))
Acount = 0
Bcount = 0

# S.sort()
# A.sort()
# B.sort()
# print(S)
# print(A)
# print(B)


com = Counter(S)
# print(com)
com1 = Counter(A)
# print(com1)
com2 = Counter(B)
# print(com2)

for string in com.keys():
    for string2 in com1.keys():
        for string3 in com2.keys():
            if string == string2:
                Acount += 1
            elif string == string3:
                Bcount += 1

if Acount > Bcount:
    print(*A)
elif Acount < Bcount:
    print(*B)
elif Acount == Bcount:
    print('パスワードをリセットしてください')
