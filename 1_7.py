# デコレーター
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_more  # デコレーター関数の指定
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)

# f = print_info(add_num)
# r = f(10, 30)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
# print(r)
