S = input()
ok = True
if len(list(S)) != len(set(S)): #重複があるかを判定することができる
    ok = False
    
if not any(s.isupper() for s in S): #すべての要素がFalseかどうかを判定
    ok = False
if not any(s.islower() for s in S): #すべての要素がFalseかどうかを判定
    ok = False
if ok:
    print("Yes")
else:
    print("No")