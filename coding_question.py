# C問題

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
first = input()
last = input()
tmp = input()

result = 'false'

is_first_coming = False
for alphabet in alphabets:
    if first == alphabet:
        is_first_coming = True

    if is_first_coming and tmp == alphabet:
        result = 'true'

    if last == alphabet:
        break

print(result)

# C問題
board = input()
result = 'D'

target = board[0]  # 最初に来た石が５回続けば勝敗が決定するけど、そうでない場合は引き分けになる
count = 0

for stone in board:
    if stone != '.' and stone == target:
        count += 1
    else:
        break

    if count == 5:
        result = target
print(result)
