# 引数で渡された文字列が回文（例「たけやぶやけた」）かどうかを判定するメソッドを書け。メソッドの引数は文字列、返り値はBoolean型とする

s = input()
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
result = is_palindrome(s)
print(result)

#　このコードのテストを書く
import unittest
from is_palindrome import is_palindrome

class Test_is_palindrome(unittest.TestCase):
    def test_is_palindrome(self):
        string = "たけやぶやけた"
        expected = True
        actual = is_palindrome(string)
        self.assertEqual(expected, actual)
   
    def test_is_not_palindrome(self):
        string = "たけやぶ"
        expected = False
        actual = is_palindrome(string)
        self.assertEqual(expected, actual)
   


if __name__ == "__main__":
    unittest.main()
