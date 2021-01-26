f = open('test.txt', 'w')
f.write('Test\n')
print('I', 'am', 'Junya', sep=' ', end='!', file=f)
f.close()


# withステートメントでファイろをopenする方法
# 上記と同じ内容をf.closeを用いないでかく
# インデント内の処理が終わったら自動的にファイルを閉じる
with open('test2.txt', 'w') as f:
    f.write('Test2\n')
    print('My', 'name', 'is', 'Junya', sep=' ', end='?', file=f)
