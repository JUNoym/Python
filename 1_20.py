# クラスの定義 初期化方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print('Hi My name is {} {}yaers old'.format(self.name, self.age))

    def __del__(self):
        print('オベジェクトが削除された時に呼ばれる関数')


person1 = Person('Junya', 22)
person1.introduction()
del person1

# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

# デコレーターについて


def Decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# このadd_num関数を受け取るデコレーターを作る


def add_num(a, b):
    return a + b


f = Decorator(add_num)  # wrapperを返してくれている
r = f(10, 50)
print(r)
