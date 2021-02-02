# 五目並べ実装　縦横斜め
board = []

for i in range(5):
    board.append(input())


def row():
    result = 'D'

    for line in board:
        target = line[0]
        count = 0

        for stone in line:
            if stone != '.' and stone == target:
                count += 1
            else:
                break
        if count == 5:
            result = target

    return result


def column():
    result = 'D'

    for i in range(5):
        target = ''
        count = 0

        for j in range(5):
            if target == '':
                target = board[j][i]

            stone = board[j][i]
            if stone != '.' and stone == target:
                count += 1
            else:
                break

        if count == 5:
            result = target
            break
    return result


def oblique():
    result = 'D'
    switch = [True, False]

    for TF in switch:
        target = ''
        count = 0

        if TF:
            j = 0
            j_diff = 1
        else:
            j = 4
            j_diff = -1

    for i in range(5):
        # 0,1,2,3,4
        stone = board[j][i]

        if target == '':
            target = stone

        if stone != '.' and stone == target:
            count += 1
        j = j + j_diff

        if count == 5:
            result = target
            break
    return result


row = row()
column = column()
oblique = oblique()

if row != "D":
    print(row)
elif column != "D":
    print(column)
elif oblique != "D":
    print(oblique)
else:
    print("D")
