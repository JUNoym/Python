l = []

while True:
    x = int(input())
    if x == 0:
        break
    l.append(x)


for i in range(len(l)):
    print(f"Case {i+1}: {l[i]}")
