# B問題
x, y, n = map(int, input().split())
dirc = ['N', 'E', 'S', 'W']
now_d = 0

for _ in range(n):
    lr = input()

    if lr == 'R':
        now_d = (now_d + 1) % 4
    else:
        now_d = (now_d + 3) % 4

    if dirc[now_d] == 'W':
        x -= 1

    elif dirc[now_d] == 'N':
        y -= 1

    elif dirc[now_d] == 'E':
        x += 1

    elif dirc[now_d] == 'S':
        y += 1

    print(x, y)

# B問題　解けた
h, w, y, x, m = map(str, input().split())
h = int(h)
w = int(w)
y = int(y)
x = int(x)

result = "Yes"
directions = ["N", "E", "S", "W"]
now_d = 0

s = [list(input()) for _ in range(h)]

if m == 'N':
    y -= 1
    if s[y][x] == '#':
        result = 'No'


elif m == 'E':
    x += 1
    if s[y][x] == '#':
        result = 'No'

elif m == 'S':
    y += 1
    if s[y][x] == '#':
        result = 'No'

elif m == 'W':
    x -= 1
    if s[y][x] == '#':
        result = 'No'


if x < 0 or x >= int(w) or y < 0 or y >= int(h):
    result = 'No'

print(result)
