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
