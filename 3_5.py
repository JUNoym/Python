# B問題　渦巻に時計回り
x, y, n = map(int, input().split())
directions = ['E', 'S', 'W', 'N']
now_direction = 0
count = 0
max_count = 1
first = True


def move(d, x, y):
    if d == 'N':
        y -= 1
    elif d == 'E':
        x += 1
    elif d == 'S':
        y += 1
    elif d == 'W':
        x -= 1
    return (x, y)


for i in range(n):
    x, y = move(directions[now_direction], x, y)
    count += 1
    if first and count == max_count:
        first = False
        count = 0
        now_direction = (1 + now_direction) % 4
    elif count == max_count:
        first = True
        count = 0
        max_count += 1
        now_direction = (1 + now_direction) % 4

print(x, y)
