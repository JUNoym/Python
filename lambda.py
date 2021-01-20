# functionを引数とするものは、lambdaを使った方がコード量が減って見やすくなる

l = ['sun', 'Mon', 'tue', 'Wed', 'Thu', 'fri', 'Sat']
l_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def change_words(words, func):
    for word in words:
        print(func(word))


def change_nums(nums, func):
    for num in nums:
        print(func(num))


# def capital_func(word):
#     return word.capitalize()

# def add_1(num):
#     return num + 1

# def capital_func(word): return word.capitalize()


# def add_1(num): return num + 1


change_words(l, lambda word: word.capitalize())
change_nums(l_num, lambda num: num + 2)

# ジェネレーター　for文で繰り返し処理したいけど、繰り返し処理する間に処理を挟みたい場合に使う
l = ['hello', 'hi', 'morning']

for i in l:
    print(i)

print('----------------------')


def counter(num=10):
    for _ in range(num):
        yield 'run'


def greeting():
    yield 'hello'
    yield 'hi'
    yield 'morning'


for g in greeting():
    print(g)

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(g))


# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r = [i for i in t if i % 2 == 0]
print(r)


r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
print(r)


# 辞書包括表記
w = ['mon', 'tue', 'wed']
t = ['cola', 'coffee', 'tea']

d = {}
for x, y in zip(w, t):
    d[x] = y
print(d)

# これを１行で包括表記すると
d = {x: y for x, y in zip(w, t)}
print(d)

# 名前空間
animal = 'cat'


def f():
    # print(animal) #local variable 'animal' referenced before assignment
    animal = 'dog'  # ローカルでanimalを定義しているからその前にanimalをprintしようとするとエラーになる
    print(animal)


f()
