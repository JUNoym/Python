n = int(input())
check = n * 1.08
check2 = int(check)

if check2 < 206:
    print("Yay!")
elif check2 == 206:
    print("so-so")
else:
    print(":(")
