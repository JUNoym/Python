i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print(j)  # [100, 2, 3, 4, 5]
print(i)  # [100, 2, 3, 4, 5]

x = [1, 2, 3, 4, 5]
y = x.copy()
# print(y)
y[0] = 100
print('x:', x)  # x: [1, 2, 3, 4, 5]
print('y:', y)  # y: [100, 2, 3, 4, 5]
