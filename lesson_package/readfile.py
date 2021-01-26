S = """\
AAA
BBB
CCC
DDD
"""
# test2.txtにSをwithを用いて書き込んだ
# with open('test2.txt', 'w') as f:
#     f.write(S)

with open('test2.txt', 'r') as f:
    # print(f.read())
    while True:
        # １行ずつ読み込む
        line = f.readline()
        print(line, end='')
        if not line:
            break


# チャンクごとに読み出すことも可能
with open('test2.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break
