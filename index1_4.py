# 辞書のコピー　参照渡し　値渡し
x = {'a': 1}
y = x
y['a'] = 1000
print(x)  # {'a': 1000}
print(y)  # {'a': 1000}

X = {'a': 1}
Y = X.copy()
Y['a'] = 1000
print(X)
print(Y)

# 集合（set）の使い所　共通点を見つけ出す時に使う
my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'N', 'D', 'E'}
print(my_friends & A_friends)  # 自分の友人とAの友人のなkで共通なものを取り出す

# リストから集合に型変換も行える
f = ['apple', 'banana', 'apple', 'banana']
f_kind = set(f)
print(f_kind)  # {'banana', 'apple'}

# １行が長くなる場合 大体80文字くらい書いたら次の行に行った方がいいと言われている
s = 'aaaaaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbb'
print(s)

# リストの中に入っているか
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 1000 not in y:
    print('Not')

is_ok = False

if not is_ok:
    print('hello')


# 値が入っているか入っていないかを判定するプログラム
# リストの中に何も入っていなければ　elseに進むし入っていればTrueになる
is_ok = [1, 2, 3]

if is_ok:
    print('値が入っている')
else:
    print('値が入っていない')

# Noneを判定する場合　== を使うのではなく is　を使うことが推奨されている
is_empty = None
if is_empty is None:
    print('None!!')


count = 0

# while count < 5:
#     print(count)
#     count += 1

while True:
    if count > 5:
        break
    if count == 2:
        count += 1
        continue  # 次の行をすっ飛ばしてループに行く
    print(count)  # 01345
    count += 1
