# 例外処理
l = [1, 2, 3]
i = 5

# del l

try:
    l[i] + 1
except IndexError as ex:
    print('catch error: {}'.format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('catch error: {}'.format(ex))
else:
    print('done')
finally:
    print('必ず実行される関数')

# 独自例外を作成
raise IndexError('test error')
