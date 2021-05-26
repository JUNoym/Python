l1 = []

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    l1.append([x, y])


l3 = []
for l2 in l1:
    l2.sort()

    l3.append(l2)


print(l3[0][0], l3[0][1])
print(l3[1][0], l3[1][1])
print(l3[2][0], l3[2][1])

# 解答
while(True):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x > y:
        x, y = y, x
    print(x, y)
