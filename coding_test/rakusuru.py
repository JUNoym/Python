# 引数で渡された文字列が回文（例「たけやぶやけた」）かどうかを判定するメソッドを書け。メソッドの引数は文字列、返り値はBoolean型とする

s = input()
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
result = is_palindrome(s)
print(result)