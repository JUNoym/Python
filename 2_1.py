
for i in range(9):
    a = i + 1
    for j in range(9):
        b = j + 1
        for k in range(9):
            c = k + 1
            if (a * 10 + b) + (c * 10 + a) == (b * 100 + b * 10 + c):
                print(a, b, c)
