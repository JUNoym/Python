# input関数
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print(next)

# for文　イテレーター
some_list = [1, 2, 3, 4, 5]

for i in some_list:
    print(i)

# 文字列でもできる
for s in 'abcde':
    print(s)

#　リストでもできる
for word in ['My', 'name', 'is', 'Mike', ]:
    print(word)


# for else文
for fruit in ['apple', 'orenge', 'banana']:
    if fruit == 'orenge':
        continue  # apple banana Done
    print(fruit)
else:
    print('Done')

# range関数
for i in range(1, 10, 2):
    print(i)

for i in range(10):
    print(i, 'hello')


# enumerate関数　for文などでインデックスを振ることができる
for i, fruit in enumerate(['apple', 'banana', 'orenge']):
    print(i+1, fruit)

# zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orenge']
drinks = ['Coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# 関数定義
def say_something():
    s = 'hi'
    return s


result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return('this is tomato')
    elif color == 'green':
        return('this is green pepper')
    else:
        return('hahaha')


def calc(num):
    num_2 = int(num) * int(num)
    return num_2


result = calc(43)
print(result)

result = what_is_this('green')
print(result)

# 位置引数とキーワード デフォルト引数


def menu(entree='beef', drink='cola', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)


menu(drink='coffee')  # beef coffee ice


# def test_func(x, l=[]):
def test_func(x, l=None):
    if l is None:
        l = []
        l.append(x)
        return l


y = [1, 2, 3]
r = test_func(100, y)
print(r)  # [1, 2, 3, 100]

y = [1, 2, 3]
r = test_func(200, y)
print(r)  # [1, 2, 3, 200]

r = test_func(100)
print(r)

r = test_func(100)
print(r)
# [100, 100] pythonではリストや辞書などの参照渡しのものをデフォルト引数として設定するのは
# バグの原因になるので推奨されていない
