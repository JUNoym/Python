# 位置引数のタプル化
def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)


say_something('hi', 'Mike', 'hoo')
# こうやってやるのはめんどくさいから


def say_something2(*args):  # 引数が何個入ってくるかわからない場合に便利
    print(args)
    for arg in args:
        print(arg)


say_something2('hi', 'Mike', 'hoo')

# キーワード引数の辞書化
#　辞書にアスタリスクをつけて引数として渡す方法


def menu(food, *args, **kwargs):
    print(food)
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)


d = {
    'entree': 'beef',
    'drink': 'coffee',
    'main': 'steak'
}

menu('banana', 'apple', 'orenge', entree='beef', drink='coffee')


# 関数内関数
def outer(a, b):
    def plus(c, d):
        return c + d
    r = plus(a, b)
    print(r)


outer(4, 5)


def outer1(a, c):
    def mutiple(m, f):
        return m * f
    r = mutiple(a, c)
    print(r)


outer1(42, 16)

# クロージャー　初めに引数を設定して、用途に応じてクロージャーを使う


# def outer(a, b):
#     def inner():
#         return a + b

#     return inner


# print(outer(1, 2))  # <function outer.<locals>.inner at 0x10136b7b8>

# f = (outer(1, 2))
# r = f()
# print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return radius * radius * pi

    return circle_area


# print(circle_area_func(5))
cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.14159265)
r = cal2(5)
print(r)
