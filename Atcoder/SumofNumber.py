while True:
    num = int(input())
    if num == 0:
        break
    ans = 0
    while num > 0:
        ans += num % 10
        num = num // 10
    print(ans)
