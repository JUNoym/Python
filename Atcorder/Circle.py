W, H, x, y, r = map(int, input().split())
ok = True
if x < r or x + r > W:
    ok = False
if y < r or y + r > H:
    ok = False
if ok:
    print("Yes")
else:
    print("No")
