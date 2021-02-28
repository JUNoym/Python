h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
# print(s)

for y in range(h):
    for x in range(w):
        # もし取り出した値が左端のマスだった場合は,その右隣が＃であれば条件を満たすので
        # その座標を表示させればいい
        # また取り出した値が右端で,その左つまりx - 1が#の場合も条件を満たす
        if x == 0 or s[y][x - 1] == '#':
            if x == w - 1 or s[y][x + 1] == '#':
                print(y, x)
