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
