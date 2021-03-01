# 座標系での移動
y, x, n = map(int, input().split())

for _ in range(n):
    direction = input()

    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1

    print(y, x)


# 座標系での移動　B問題
y, x, D = map(str, input().split())
d = input()

if D == "N":
    if d == "R":
        x = int(x) + 1
    elif d == "L":
        x = int(x) - 1

if D == "W":
    if d == "R":
        y = int(y) - 1
    elif d == "L":
        y = int(y) + 1

if D == "S":
    if d == "R":
        x = int(x) - 1
    elif d == "L":
        x = int(x) + 1

if D == "E":
    if d == "R":
        y = int(y) + 1
    elif d == "L":
        y = int(y) - 1


print(y, x)
