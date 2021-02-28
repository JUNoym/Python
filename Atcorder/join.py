test = ['ab', 'c', 'de']
result = " "
for i in test:
    print(i)
    result += i

print(result)

# 上記と同じことをjoinでやることができる

print('---------------------------------')

test2 = ['sdf', 'ert', 'fgj']
result2 = ''.join(test2)
print(result2)

print('---------------------------------')

result3 = '$'.join(test2)
print(result3)

print('---------------------------------')

test = ['wer', 'rre', 'tte', 56]
map_result = map(str, test)
result = ''.join(map_result)
print(result)

print('---------------------------------')

lists = [[423], [234], [345]]
map_result = map(str, lists)
result = []
print(lists)
for i in lists:
    result += i
print(result)
print(result[0])
