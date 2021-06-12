while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0

    for i in range(1, n+1):  # 1,2,3,4,5
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i+j+k == x:
                    count += 1
                    print()
    print(count)
