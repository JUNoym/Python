import math
while True:
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if op == "?":
        break
    if op == "+":
        print(math.floor(a + b))
    elif op == "*":
        print(math.floor(a * b))
    elif op == "/":
        print(math.floor(a / b))
    else:
        print(math.floor(a - b))
