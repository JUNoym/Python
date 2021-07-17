A, B, C, D = map(int, input().split())
blue, red = A+B, C
for i in range(10**8):
    if blue <= red*D:
        print(i+1)
        exit()
    blue += B
    red += C
print(-1)
